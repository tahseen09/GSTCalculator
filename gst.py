class GST:
    ROUND_OFF_PLACES = 2
    
    def __init__(self, unit_price, category):
        self.unit_price = unit_price
        self.category = category
        self.gst_value = self.calculate_gst()
    
    def calculate_gst(self):
        GST_SLABS_PERCENT = {"food-grains": 0, "furniture": 5, "electronics": 18, "cosmetics": 28}
        GST_RATE = GST_SLABS_PERCENT[self.category]/100
        gst_amount_per_unit = round(self.unit_price*GST_RATE, self.ROUND_OFF_PLACES)
        return gst_amount_per_unit

    def print_gst(self):
        print("GST applicable per unit: "+str(self.gst_value))
