from fastapi import FastAPI
from elasticsearch import Elasticsearch

app = FastAPI()

es = Elasticsearch(
    "https://localhost:9200",
    basic_auth=("elastic", "O-SUrWaXssvbiszLuxxN"),
    verify_certs=False
)

@app.get("/")
def home():
    return {"message": "Search engine API running"}

@app.get("/search")
def search(q: str):
    result = es.search(
        index="webpages",
        query={
            "multi_match": {
                "query": q,
                "fields": ["title", "content"]
            }
        }
    )

    hits = []
    for h in result["hits"]["hits"]:
        hits.append(h["_source"])

    return {"results": hits}