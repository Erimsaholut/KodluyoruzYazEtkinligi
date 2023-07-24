cost = float(input("Cost: "))
price = float(input("Price: "))

while cost >= price:
    print("Error: Cost should be lower than Price.")
    cost = float(input("Cost: "))
    price = float(input("Price: "))

profit = price - cost
needed_items = int(profit / (price - cost))

print("Number of items to be sold for a profit:", needed_items)
