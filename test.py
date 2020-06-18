import unittest
from gst import GST
from amount import TotalAmount

class TestGst(unittest.TestCase):

    def test_gst_food(self):
        gst_obj = GST(100, "food-grains")
        self.assertEqual(gst_obj.calculate_gst(), 0.0, "Should be 0")

    def test_gst_furniture(self):
        gst_obj = GST(20000, "furniture")
        self.assertEqual(gst_obj.calculate_gst(), 1000, "Should be 1000")

    def test_gst_cosmetics(self):
        gst_obj = GST(200, "cosmetics")
        self.assertEqual(gst_obj.calculate_gst(), 56, "Should be 256")

    def test_gst_electronics(self):
        gst_obj = GST(5000, "electronics")
        self.assertEqual(gst_obj.calculate_gst(), 900, "Should be 900")

    def test_amount(self):
        amount_obj = TotalAmount(900, 2, 5000)
        self.assertEqual(amount_obj.amount, 11800, "Must be 11800")

    
unittest.main()