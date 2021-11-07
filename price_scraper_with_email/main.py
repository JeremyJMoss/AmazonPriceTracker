import pandas
from web_scraper import WebScraper
from price_comparer import PriceComparer
from email_client import EmailClient
from datetime import datetime

today = datetime.now().strftime("%d/%m/%Y")
data_dict = {"date": []}
message = ""
url_list = pandas.read_csv("../url_file.txt")
url_list = url_list.to_dict("list")
url_list.pop("Unnamed: 0")

for num in range(0, len(url_list["url"])):
    web_scraper = WebScraper(url_list["url"][num])
    current_price = web_scraper.return_current_price()
    input_price = int(url_list["price"][num].replace("$", ""))
    try:
        file = pandas.read_csv("price_over_time.txt")
    except FileNotFoundError:
        pass
    else:
        data_dict = file.to_dict("list")
        data_dict.pop("Unnamed: 0")
    finally:
        if not data_dict["date"]:
            data_dict["date"].append(today)
        for item in data_dict["date"]:
            if item != today:
                data_dict["date"].append(today)
        for header in data_dict:
            if header == web_scraper.return_title():
                header.append[current_price]
            else:
                data_dict[web_scraper.return_title()] = []
                data_dict[web_scraper.return_title()].append(current_price)
                break


    # Price comparer class takes in current price and compares it to user inputted price from url_file.txt
    price_comparer = PriceComparer(current_price, input_price)
    if price_comparer.compare_prices():
        message += f"{web_scraper.return_title()}\n" \
                   f"We have found that this item has dropped below your wanted price\n" \
                   f"Your wanted price: ${input_price}\n" \
                   f"Current price: ${current_price}\n" \
                   f"The time is now to buy go to <a href={url_list['url'][num]}>this link</a>\n\n"
    else:
        pass

df = pandas.DataFrame(data_dict)
df.to_csv("price_over_time.txt")
if message != "":
    email = EmailClient()
    email.send_email(message)
