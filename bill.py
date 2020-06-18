from gst import GST
from amount import TotalAmount

class Bill:

    def __init__(self, product):
        self.product = product

    def print_bill(self):
        gst_obj = GST(unit_price=self.product.unit_price, category=self.product.category)
        gst_obj.print_gst()
        amount = TotalAmount(gst=gst_obj.gst_value, quantity=self.product.quantity, unit_price=self.product.unit_price)
        amount.print_amount()
        