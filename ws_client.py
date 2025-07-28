import asyncio
import json
from pprint import pprint
from xml.etree.ElementTree import indent
import websockets
from datetime import datetime
#
async def subscribe(channel, target_currency="BTC", quote_currency="KRW"):
    """https://docs.coinone.co.kr/reference/public-websocket-1"""
    uri = "wss://stream.coinone.co.kr"
    request = {
        "request_type": "SUBSCRIBE",
        "channel": channel,  # TICKER, TRADE, ORDERBOOK
        "topic": {"quote_currency": quote_currency, "target_currency": target_currency},
    }
    request = json.dumps(request)
    async with websockets.connect(uri) as websocket:
        datetime_start = datetime.now()
        datetime_end = datetime.now()
        await websocket.send(request)
        #
        while True:
            datetime_end = datetime.now()
            diff_secs = int((datetime_end - datetime_start).total_seconds())
            #print("diff_secs:", diff_secs)
            #print("datetime_start:", datetime_start)
            #print("datetime_end:  ", datetime_end)
            if diff_secs > 60:
                print("PING", diff_secs)
                await websocket.send('{"request_type": "PING"}')
                #await asyncio.sleep(0.1 - diff_secs)
                datetime_start = datetime_end
            #
            response = await websocket.recv()
            response_json = json.loads(response)
            #pprint(response_json)
            if 'data' in response_json and 'last' in response_json['data']:
                print(diff_secs, 'last:',json.dumps(response_json['data']['last'], indent=2, ensure_ascii=False))
                print(json.dumps(response_json['data'], indent=2, ensure_ascii=False))
            if response_json["response_type"] == "ERROR":
                print("error_code", response_json["error_code"])
            if response_json["response_type"] == "PONG":
                print("PONG received", response_json)
            #
        #
    #
#
async def gather():
    await asyncio.gather(
        #subscribe("TRADE"),
        subscribe("TICKER", target_currency="ETH", quote_currency="KRW"),
        #subscribe("ORDERBOOK"),
    )
#
if __name__ == '__main__':
    asyncio.run(gather())
#
# 출처: https://comdoc.tistory.com/entry/파이썬-코인원-웹-소켓-데모 [ComDoc:티스토리]
