class Item:
    def __init__(self, name, unit_price, quantity):
        self.unit_price = float(unit_price)
        self.name = name.lower()
        self.quantity = int(quantity)
        self.category = self.get_category()

    def get_category(self):
        categories = ["food", "furniture", "electronics", "cosmetics"]
        
        category_items = [["rice", "wheat", "dal"], ["table", "sofa", "chair"], ["mobile", "tv", "tablet"], ["cream", "perfume", "lotion"]]
        
        l = len(category_items)
        
        for i in range(l):
            if self.name in category_items[i]:
                return categories[i]
        
        return None