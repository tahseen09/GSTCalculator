class Item:
    def __init__(self, name, unit_price, quantity):
        self.unit_price = float(unit_price)
        self.name = name.lower()
        self.quantity = int(quantity)
        self.category = self.get_category()

    def get_category(self):

        categories = {
            "food-grains": ["rice", "wheat", "dal"],
            "furniture": ["table", "sofa", "chair"],
            "electronics": ["mobile", "tv", "tablet"],
            "cosmetics": ["cream", "perfume", "lotion"]
        }
        for key, value in categories.items():
            if self.name in value:
                return key

        return None
