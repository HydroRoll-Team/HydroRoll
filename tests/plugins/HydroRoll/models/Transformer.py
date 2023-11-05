import requests

API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
