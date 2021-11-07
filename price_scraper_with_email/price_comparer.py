

class PriceComparer:

    def __init__(self, cur_price, input_price):
        self.sale_price = cur_price
        self.inputted_price = input_price

    def compare_prices(self):
        return self.sale_price <= self.inputted_price

