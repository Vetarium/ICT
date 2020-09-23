days = int(input(" Insert days "))
hours = int(input("insert hours "))
min = int(input("Insert minutes "))
sec = int(input("Insert seconds "))

total_sec = (days * 24 * 3600) + (hours* 3600)+(min*60) + sec
print("Total amount of seconds equal",  total_sec)