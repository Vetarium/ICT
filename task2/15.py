#fibboncci
a = int(input("Insert the number "))
f0 = 0
f1 = 1
f2 = 1
chk = False

i = 3;
f_sum = 0;
while f_sum < a:
    f_sum = f1 + f2
    f1 = f2
    f2 = f_sum
    if a == f_sum:
        print(i)
        chk = True

    else:
        i = i + 1

if chk == False:
    print(-1)
