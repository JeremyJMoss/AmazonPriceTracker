from bs4 import BeautifulSoup
import requests


class WebScraper:

    def __init__(self, url):
        self.response = requests.get(url)
        self.soup = BeautifulSoup(self.response.text, "html.parser")

    def return_current_price(self):
        price = self.soup.find(class_="a-offscreen").get_text().replace("$", '')
        return float(price)

    def return_title(self):
        title = self.soup.select_one(selector="#productTitle").get_text().strip()
        return title
