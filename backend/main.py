import json
from fastapi import FastAPI
from scraper import Scraper
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from supabase import create_client, Client
from starlette.responses import Response

# Add supabase url and key below
url = ''
key = ''

supabase: Client = create_client(url, key)

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
    scrape_data = supabase.table('scrape').select(
        '*').filter('url', 'eq', req.url).execute()

    if (len(scrape_data.data) > 0):
        return str(scrape_data.data[0]['scrape_html'])

    scrapped_data = quotes.scrapedata(req)

    try:
        supabase.table('scrape').insert(
            {'url': req.url, 'scrape_html': str(scrapped_data)}).execute()
    except:
        pass

    return scrapped_data
