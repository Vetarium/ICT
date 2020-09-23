cents = int(input("Insert qty of cents: "))

toonies = int(cents / 200)
cents -= toonies * 200

loonies = int(cents / 100)
cents -= loonies * 100

quarters = int(cents / 25)
cents -= quarters * 25

dimes = int(cents / 10)
cents -= dimes * 10

nickels = int(cents / 5)
pennies = cents

print("Change is" ,toonies, "toonies", loonies, "loonies" , quarters, "quarters",dimes,"dimes",nickels,"nickels",pennies, "pennies")