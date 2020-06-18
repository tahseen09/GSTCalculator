from product import Item
from bill import Bill

def start():
    print("Please Provide Your Order in the mentioned format:\n <quantity> <name of item> <price of each item>")
    order = input().split(' ')
    name = order[1]
    unit_price = order[2]
    quantity = order[0]

    item = Item(name=name, unit_price=unit_price, quantity=quantity)

    if item.category is None:
        print("Item not in inventory")

    else:
        bill = Bill(item)
        bill.print_bill()

start()