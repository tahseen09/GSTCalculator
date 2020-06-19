class TotalAmount:
    ROUND_OFF_PLACES = 2
    def __init__(self, gst, quantity, unit_price):
        self.gst = gst
        self.unit_price = unit_price
        self.quantity = quantity
        self.amount = self.calculate_amount()


    def calculate_amount(self):
        return round((self.unit_price+self.gst)*self.quantity, self.ROUND_OFF_PLACES)

    def print_amount(self):
        print("Final Price: "+str(self.amount))
