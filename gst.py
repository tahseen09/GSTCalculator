class GST:

    def __init__(self, unit_price, category):
        self.unit_price = unit_price
        self.category = category
        self.gst = self.calculate_gst()
    
    def calculate_gst(self):
        gst_rates = {"food": 0, "furniture": 5, "electronics": 18, "cosmetics": 28}
        gst_rate = gst_rates[self.category]
        gst_amount_per_unit = round(self.unit_price*(gst_rate/100), 2)
        return gst_amount_per_unit

    def print_gst(self):
        print("GST applicable per unit: "+str(self.gst))