cash = float(input())

for i in range(3):
    cash = cash*1.04
    cash = float('{:.2f}'.format(cash))
    print("for the ",i,"year sum will be ",cash)