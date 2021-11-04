from tkinter import *


class AmazonItemAdder:

    def __init__(self):
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

    def show_items(self):


    def submit_to_form(self):
        pass
