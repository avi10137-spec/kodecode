from fastapi import FastAPI
import uvicorn
import requests
import requests
response = requests.get("http://localhost:8000/5")

print(response.status_code)
print(response.json())