from product import Item
from bill import Bill

order = input().split(' ')
name = order[1]
unit_price = order[2]
quantity = order[0]

item = Item(name=name, unit_price=unit_price, quantity=quantity)

if item.category is None:
    print("Item not in inventory")

else:
    bill = Bill(item)
    bill.get_bill()