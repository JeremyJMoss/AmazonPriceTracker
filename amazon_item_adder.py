from tkinter import *
import pandas
from tkinter import messagebox


class AmazonItemAdder:

    def __init__(self):
        try:
            self.url_entries = pandas.read_csv("url_file.txt")
        except FileNotFoundError:
            self.url_entries = {"url": [], "price": []}
        else:
            self.url_entries = self.url_entries.to_dict(orient="records")
            self.url_entries[0].pop("Unnamed: 0")
            self.url_entries = self.url_entries[0]
            if isinstance(self.url_entries["url"], str):
                self.url_entries["url"] = [self.url_entries["url"]]
                self.url_entries["price"] = [self.url_entries["price"]]
            else:
                pass
        self.root = Tk()
        self.root.title("Amazon Price Tracker")
        self.root.config(padx=20, pady=20)
        self.url_label = Label(text="Enter url of Amazon item to track price", font=("Arial", 14, "normal"))
        self.url_label.grid(row=0, column=0, columnspan=2, pady=5)
        self.entry_url = Entry(justify="center", width=60, font=("Arial", 12, "normal"))
        self.entry_url.grid(row=1, column=0, columnspan=2, pady=5)
        self.price_label = Label(text="Enter maximum price willing to pay for said item", font=("Arial", 14, "normal"))
        self.price_label.grid(row=2, column=0, pady=10)
        self.entry_price = Entry(justify="center", width=8, font=("Arial", 14, "normal"))
        self.entry_price.grid(row=2, column=1, pady=10)
        self.submit = Button(text="Submit", font=("Arial", 14, "bold"), command=self.submit_to_form)
        self.submit.grid(row=3, column=0, columnspan=2, pady=5)
        self.show_list = Button(text="Show tracked url's", font=("Arial", 12, "bold"), command=self.show_items)
        self.show_list.grid(row=4, column=0, columnspan=2,  pady=20)
        self.root.mainloop()

    def check_list_existence(self):
        try:
            pandas.read_csv("url_file.txt")
        except FileNotFoundError:
            messagebox.showwarning(title="No Url Found", message="No url found for tracking in database")
            return False
        else:
            return True

    def stringify_url_list(self):
        url_list = pandas.read_csv("url_file.txt")
        return url_list

    def show_items(self):
        if self.check_list_existence():
            window = Tk()
            window.title("Url List")

    def submit_to_form(self):
        url = self.entry_url.get()
        self.entry_url.delete(0, END)
        price = f"${self.entry_price.get()}"
        self.entry_price.delete(0, END)
        self.url_entries["url"].append(url)
        self.url_entries["price"].append(price)
        df = pandas.DataFrame(self.url_entries)
        df.to_csv("url_file.txt")
