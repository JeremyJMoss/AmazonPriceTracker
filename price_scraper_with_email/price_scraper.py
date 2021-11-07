from bs4 import BeautifulSoup
import requests


class PriceScraper:

    def __init__(self, url):
        self.response = requests.get(url)
        print(self.response)