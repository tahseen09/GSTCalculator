import unittest
from gst import GST
from amount import TotalAmount

class TestGst(unittest.TestCase):

    def test_gst_food(self):
        UNIT_PRICE = 100
        CATEGORY = "food-grains"
        gst_obj = GST(UNIT_PRICE, CATEGORY)
        self.assertEqual(gst_obj.calculate_gst(), 0.0, "Should be 0")

    def test_gst_furniture(self):
        UNIT_PRICE = 20000
        CATEGORY = "furniture"
        gst_obj = GST(UNIT_PRICE, CATEGORY)
        self.assertEqual(gst_obj.calculate_gst(), 1000, "Should be 1000")

    def test_gst_cosmetics(self):
        UNIT_PRICE = 200
        CATEGORY = "cosmetics"
        gst_obj = GST(UNIT_PRICE, CATEGORY)
        self.assertEqual(gst_obj.calculate_gst(), 56, "Should be 256")

    def test_gst_electronics(self):
        UNIT_PRICE = 5000
        CATEGORY = "electronics"
        gst_obj = GST(UNIT_PRICE, CATEGORY)
        self.assertEqual(gst_obj.calculate_gst(), 900, "Should be 900")

    def test_amount(self):
        GST_PER_UNIT = 900
        QUANTITY = 2
        PRICE_PER_UNIT = 5000
        amount_obj = TotalAmount(GST_PER_UNIT, QUANTITY, PRICE_PER_UNIT)
        EXPECTED_VALUE = 11800
        self.assertEqual(amount_obj.amount, EXPECTED_VALUE, "Should be "+str(EXPECTED_VALUE))

    
unittest.main()