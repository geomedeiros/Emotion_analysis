from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

sentiment_analysis = pipeline("sentiment-analysis")

class TextInput(BaseModel):
    text: str

@app.post("/analyze_sentiment")
async def analyze_sentiment(input: TextInput):
    # Realiza a análise de sentimento
    result = sentiment_analysis(input.text)
    return {"text": input.text, "sentiment": result[0]}

# Executa o servidor
# Comando para iniciar o servidor: uvicorn main:app --reload
