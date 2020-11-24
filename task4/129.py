import random

s = []
for x in range(0, 1000):
    s.append(random.randint(2, 12))

cnt_2 = s.count(2)
cnt_3 = s.count(3)
cnt_4 = s.count(4)
cnt_5 = s.count(5)
cnt_6 = s.count(6)
cnt_7 = s.count(7)
cnt_8 = s.count(8)
cnt_9 = s.count(9)
cnt_10 = s.count(10)
cnt_11 = s.count(11)
cnt_12 = s.count(12)

prob = {
    "2": (cnt_2 / 1000) * 100,
    "3": (cnt_3 / 1000) * 100,
    "4": (cnt_4 / 1000) * 100,
    "5": (cnt_5 / 1000) * 100,
    "6": (cnt_6 / 1000) * 100,
    "7": (cnt_7 / 1000) * 100,
    "8": (cnt_8 / 1000) * 100,
    "9": (cnt_9 / 1000) * 100,
    "10": (cnt_10 / 1000) * 100,
    "11": (cnt_11 / 1000) * 100,
    "12": (cnt_12 / 1000) * 100
}

calcprob = {
    "2": 2.78,
    "3": 5.56,
    "4": 8.33,
    "5": 11.11,
    "6": 13.89,
    "7": 16.67,
    "8": 13.89,
    "9": 11.11,
    "10": 8.33,
    "11": 5.56,
    "12": 2.78
}
p = ""
for x in range(2, 13):
    p = str(x) + "                  " + str(prob[str(x)]) + "                       " + str(calcprob[str(x)])
    print(p)
    p = ""