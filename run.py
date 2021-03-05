import uvicorn
from fastapi import FastAPI

from typing import List
from pydantic import BaseModel
import pandas as pd

from config.config import Settings
from loader.get_model import get_model
from loader.get_metrics import show_metrics
from validation.validation_body import request_body

settings = Settings()
model = get_model(settings.version)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/info/")
async def root():
    return model['tags']

@app.get("/metrics/")
async def root():
    return show_metrics(model['metrics'])

@app.post('/predict')
async def predict(data: request_body):
    df = pd.DataFrame([dict(data)])
    pred = model['model'].predict(df)
    return {
        "probabilities": list(pred),
        "length": len(pred),
        "version": settings.version,
    }

if __name__ == "__main__":
    uvicorn.run(app)
