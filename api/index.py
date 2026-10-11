from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    regions: List[str]
    threshold_ms: float

data = {
    "apac": {"avg_latency": 196.87, "p95_latency": 219.59, "avg_uptime": 97.942, "breaches": 10},
    "emea": {"avg_latency": 191.34, "p95_latency": 236.52, "avg_uptime": 98.519, "breaches": 9},
    "amer": {"avg_latency": 182.93, "p95_latency": 224.1, "avg_uptime": 98.09, "breaches": 7}
}

@app.post("/")
@app.post("/api")
def get_metrics(q: Query):
    results = []
    for r in q.regions:
        if r in data:
            results.append({"region": r, **data[r]})
    return {"regions": results}
