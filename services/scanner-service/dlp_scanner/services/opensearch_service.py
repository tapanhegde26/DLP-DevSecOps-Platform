from opensearchpy import OpenSearch
import os

client = OpenSearch(
    hosts=[{
        "host": os.getenv("OPENSEARCH_HOST", "localhost"),
        "port": 9200
    }],
    http_compress=True
)


def store_incident(document):

    response = client.index(
        index="dlp-incidents",
        body=document
    )

    return response
