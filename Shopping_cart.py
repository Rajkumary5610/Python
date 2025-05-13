# shopping cart programme

items = []
prices = []

total = 0

while True:
    item = input("Enter the item to buy (q to quit): ")
    if item == "q":
        break
    else:
        price = float(input("Enter the {item} price: $"))
        items.append(item)
        prices.append(price)
print("------Your items-----")


for item in items:
    for price in prices:
        print(f"{item}:{price}")
        break
for price in prices:
    total = total + price

print(f"your total items prices : ${total}")
