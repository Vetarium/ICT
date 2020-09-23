loaves = int(input("Amount of loaves: "))

price = loaves*3.49
discount = price*0.6
total_price = price - discount

print("Regular price of the bread", round(price,2))
print("Value of discount:", discount)
print("Total price:", total_price)