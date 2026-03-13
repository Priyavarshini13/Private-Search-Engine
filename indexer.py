from elasticsearch import Elasticsearch
import json

es = Elasticsearch(
    "https://localhost:9200",
    basic_auth=("elastic", "O-SUrWaXssvbiszLuxxN"),
    verify_certs=False
)

index_name = "webpages"
file_path = "crawler/webcrawler/webcrawler/pages.json"

with open(file_path, "r", encoding="utf-8") as f:
    first = f.read(1)
    if first != "[":
        raise ValueError("Expected JSON array")

    buffer = ""
    depth = 0

    while True:
        char = f.read(1)
        if not char:
            break

        if char == "{":
            depth += 1

        if depth > 0:
            buffer += char

        if char == "}":
            depth -= 1
            if depth == 0:
                page = json.loads(buffer)
                es.index(index=index_name, document=page)
                buffer = ""

print("Indexing complete!")