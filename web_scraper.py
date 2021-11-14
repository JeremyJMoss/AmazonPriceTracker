from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os


class WebScraper:

    def __init__(self, url):
        self.url = url
        self.options = Options()
        self.options.headless = True
        self.ex_path = os.getenv("CHROME_DRIVER")
        self.driver = webdriver.Chrome(executable_path=self.ex_path, options=self.options)
        self.driver.get(url=self.url)

    def return_current_price(self):
        price = self.driver.find_element(By.CSS_SELECTOR, ".a-text-price [aria-hidden='true']")
        price_text = price.text.replace("$", '')
        return float(price_text)

    def return_title(self):
        title = self.driver.find_element(By.ID, "productTitle")
        title_text = title.text
        return title_text
