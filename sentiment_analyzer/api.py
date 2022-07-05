from fastapi import FastAPI, Depends
from pydantic import BaseModel

from .model import get_model, Model

app = FastAPI()

class SentimentRequest(BaseModel):
    text: str


class SentimentResponse(BaseModel):
    label: str
    score: float

    
@app.post("/predict", response_model=SentimentResponse)
def predict(request: SentimentRequest, model: Model = Depends(get_model)):
    label, score = model.predict(request.text)
    return SentimentResponse(
        label=label, score=score
    )