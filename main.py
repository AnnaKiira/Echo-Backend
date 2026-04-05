from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
import httpx

load_dotenv()
api_key = os.environ.get('NEWS_API_KEY')

app = FastAPI()

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def read_root():
    return {"status": "OK"}

@app.get("/newsarticles")
def get_news_articles():
    response = httpx.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}")
    return response.json()