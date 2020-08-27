number_of_items = int(input("Number of items: "))

total_cost = 0
for i in range(number_of_items):
    item_price = int(input("Price of item: "))
    total_cost = total_cost + item_price

if total_cost < 100:
    print("Total price for", number_of_items, "items is", total_cost)
else:
    total_cost = total_cost - (total_cost * .10)
    print("Total price for", number_of_items, "items is", total_cost)