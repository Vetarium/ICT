# 1 kWh = 3.6 * 10^6 J
mass = float(input("Insert the mass in kilograms "))
dt = float(input("Insert the change of temperature "))

q = 4186 * mass * dt

cost = q/(3.6 * 10**6) *8.9

print("The energy to boil this mass is equal ",q, "Joules, and costs",cost, "cents")
