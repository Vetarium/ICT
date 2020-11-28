#this task from my HW 3
#even = female
#odd = gay
s = input()

ans = set(s)
if len(ans) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")