import requests

response = requests.post("http://127.0.0.1:8000/analyze_sentiment", json={"text": "Estou feliz!"})
print(response.json())
