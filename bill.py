from gst import GST
from amount import TotalAmount

class Bill:

    def __init__(self, product):
        self.product = product

    def get_bill(self):
        gst_obj = GST(unit_price=self.product.unit_price, category=self.product.category)
        gst_obj.print_gst()
        amount = TotalAmount(gst_obj.gst, self.product.quantity, self.product.unit_price)
        amount.print_amount()
        