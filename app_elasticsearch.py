from elasticsearch import Elasticsearch, helpers # type: ignore
# This code connects to an Elasticsearch instance and performs operations like creating, deleting, and indexing documents.
# Make sure to install the elasticsearch package using pip if you haven't already:
# pip install elasticsearch
# Replace the URL and API key with your own Elasticsearch instance details.
# The URL should point to your Elasticsearch instance, and the API key should be your authentication key
# for accessing the instance.
# The following code snippet demonstrates how to connect to an Elasticsearch instance, check its info,
# and perform some basic operations like creating an index, deleting an index, and indexing documents.
# Note: Uncomment the lines below to perform the operations as needed.
# Ensure you have the necessary permissions to perform these operations on your Elasticsearch instance.
# Import the necessary modules from the elasticsearch package
import json
import pprint
client = Elasticsearch(
    "https://8246037a32d94ddc9f740363b7ed26a5.us-central1.gcp.cloud.es.io:443",
    api_key="WC1Pa0s1Z0J5MDJ4YlEzSU9rcTQ6X3VnT0ZiNVZ4bmdMTEltU2NOOXZFQQ=="
)
# Check if the connection to the Elasticsearch instance is successful
# ObjectApiResponse를 딕셔너리로 변환
pprint.pprint(client.info().body)  # Print the info of the Elasticsearch instance
#
# Uncomment the following line to create an index if it doesn't exist
# client.indices.create(index="search-r2s6", ignore=400)
# Uncomment the following lines to delete an index if it exists
# client.indices.delete(index="search-r2s6", ignore=[400, 404])
# Uncomment the following lines to index documents
# helpers.bulk(client, docs, index=index_name)
index_name = "search-r2s6"
docs = [
    {
        "fulltext": "Yellowstone National Park is one of the largest national parks in the United States. It ranges from the Wyoming to Montana and Idaho, and contains an area of 2,219,791 acress across three different states. Its most famous for hosting the geyser Old Faithful and is centered on the Yellowstone Caldera, the largest super volcano on the American continent. Yellowstone is host to hundreds of species of animal, many of which are endangered or threatened. Most notably, it contains free-ranging herds of bison and elk, alongside bears, cougars and wolves. The national park receives over 4.5 million visitors annually and is a UNESCO World Heritage Site."
    },
    {
        "fulltext": "Yosemite National Park is a United States National Park, covering over 750,000 acres of land in California. A UNESCO World Heritage Site, the park is best known for its granite cliffs, waterfalls and giant sequoia trees. Yosemite hosts over four million visitors in most years, with a peak of five million visitors in 2016. The park is home to a diverse range of wildlife, including mule deer, black bears, and the endangered Sierra Nevada bighorn sheep. The park has 1,200 square miles of wilderness, and is a popular destination for rock climbers, with over 3,000 feet of vertical granite to climb. Its most famous and cliff is the El Capitan, a 3,000 feet monolith along its tallest face."
    },
    {
        "fulltext": "Rocky Mountain National Park  is one of the most popular national parks in the United States. It receives over 4.5 million visitors annually, and is known for its mountainous terrain, including Longs Peak, which is the highest peak in the park. The park is home to a variety of wildlife, including elk, mule deer, moose, and bighorn sheep. The park is also home to a variety of ecosystems, including montane, subalpine, and alpine tundra. The park is a popular destination for hiking, camping, and wildlife viewing, and is a UNESCO World Heritage Site."
    }
]
#bulk_response = helpers.bulk(client, docs, index=index_name)
#print(bulk_response)
