# from requests_html import HTMLSession

# class Scraper():

#     def scrapedata(self, req):
#         print(req)
#         url = f'{req.url}'

#         s = HTMLSession()
#         r = s.get(url)
#         print(r.text)

#         return r.text


# quotes = Scraper()

import requests
from bs4 import BeautifulSoup
import sys


class Scraper():

    def scrapedata(self, req):
        page = requests.get(req.url)
        soup = BeautifulSoup(page.content, 'html.parser')
        claim_sect = soup.find('section')

        find_text = soup.find_all(text='Rounded gradient')
        print(find_text)

        return str(claim_sect)


quotes = Scraper()
