class TotalAmount:

    def __init__(self, gst, quantity, unit_price):
        self.gst = gst
        self.unit_price = unit_price
        self.quantity = quantity
        self.amount = self.calculate_amount()


    def calculate_amount(self):
        return round((self.unit_price+self.gst)*self.quantity, 2)

    def print_amount(self):
        print("Final Price: "+str(self.amount))
