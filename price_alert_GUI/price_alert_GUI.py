from tkinter import *
import pandas
from tkinter import messagebox
import webbrowser
import requests


def callback(url):
    webbrowser.open(url)


def check_list_existence():
    try:
        pandas.read_csv("url_file.txt")
    except FileNotFoundError:
        messagebox.showwarning(title="No Url Found", message="No url found for tracking in database")
        return False
    else:
        return True


def stringify_url_list():
    url_list = pandas.read_csv("url_file.txt")
    url_list = url_list.to_dict("list")
    url_list.pop("Unnamed: 0")
    return url_list


def show_items():
    if check_list_existence():
        window = Tk()
        window.config(padx=20, pady=20)
        window.title("Url List")
        header = Label(window, text="Price Tracked URL's", font=("Arial", 14, "bold", "underline"))
        header.grid(row=0, column=0, columnspan=2, pady=10)
        url_list = stringify_url_list()
        column = 0
        row = 1
        for item in url_list:
            for data in url_list[item]:
                if item == "price":
                    font_style = ("Arial", 12, "bold")
                    fg = "black"
                else:
                    font_style = ("Arial", 12, "normal", "underline")
                    fg = "blue"
                label = Label(window, text=data, font=font_style, fg=fg)
                label.grid(row=row, column=column, pady=5, padx=40)
                if item == "url":
                    label.bind("<Button-1>", lambda e: callback(data))
                    label.config(cursor="hand1")
                row += 1
            column += 1
            row = 1


def submit_to_form():
    try:
        int(entry_price.get())
        response = requests.get(entry_url.get())
        response.raise_for_status()
    except TypeError:
        messagebox.showerror(title="Error",
                             message="Please enter a number")
    except (requests.exceptions.ConnectionError, requests.exceptions.InvalidURL, requests.exceptions.ConnectionError,
            requests.exceptions.SSLError, requests.exceptions.MissingSchema, requests.exceptions.HTTPError):
        messagebox.showerror(title="URL Not Found", message="Please enter a valid URL")
    else:
        url = entry_url.get()
        entry_url.delete(0, END)
        price = f"${entry_price.get()}"
        entry_price.delete(0, END)
        url_entries["url"].append(url)
        url_entries["price"].append(price)
        df = pandas.DataFrame(url_entries)
        df.to_csv("url_file.txt")


try:
    url_entries = pandas.read_csv("url_file.txt")
except FileNotFoundError:
    url_entries = {"url": [], "price": []}
else:
    url_entries = url_entries.to_dict(orient="records")
    url_entries[0].pop("Unnamed: 0")
    url_entries = url_entries[0]
    if isinstance(url_entries["url"], str):
        url_entries["url"] = [url_entries["url"]]
        url_entries["price"] = [url_entries["price"]]
    else:
        pass
root = Tk()
root.title("Amazon Price Tracker")
root.config(padx=20, pady=20)
url_label = Label(text="Enter url of Amazon item to track price", font=("Arial", 14, "normal"))
url_label.grid(row=0, column=0, columnspan=2, pady=5)
entry_url = Entry(justify="center", width=60, font=("Arial", 12, "normal"))
entry_url.grid(row=1, column=0, columnspan=2, pady=5)
price_label = Label(text="Enter maximum price willing to pay for said item", font=("Arial", 14, "normal"))
price_label.grid(row=2, column=0, pady=10)
entry_price = Entry(justify="center", width=8, font=("Arial", 14, "normal"))
entry_price.grid(row=2, column=1, pady=10)
submit = Button(text="Submit", font=("Arial", 14, "bold"), command=submit_to_form)
submit.grid(row=3, column=0, columnspan=2, pady=5)
show_list = Button(text="Show tracked url's", font=("Arial", 12, "bold"), command=show_items)
show_list.grid(row=4, column=0, columnspan=2,  pady=20)
root.mainloop()



