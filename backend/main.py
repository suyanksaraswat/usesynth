from fastapi import FastAPI
from scraper import Scraper
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()
quotes = Scraper()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ScrapperReq(BaseModel):
    url: str

@app.post("/scrapper")
async def scrape_by_url(req: ScrapperReq):
    return quotes.scrapedata(req)
