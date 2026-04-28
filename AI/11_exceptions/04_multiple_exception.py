def process_order(item, quantity):
    try:
        price = {"masala": 20}[item]
        total = price * quantity
        print(f"Total cost is {total}")
    except KeyError:
        print("Sorry that chai is not on menu")
    except TypeError:
        print("Quantity must be in number")

process_order("ginger", 20)
process_order("masala", "two")