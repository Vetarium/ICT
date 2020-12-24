#Seatle to sanfran and back FS = fransisco to seatle ts (to seatle)
#Seatle to farncisco SF = fs (from seatle)
days = int(input())
string = input()
arr = list(string)
fs = 0;
ts = 0;

for i in range(1, days):
    if(arr[i-1] == "F" and arr[i] == "S"):
        ts = ts + 1 #to seatle

    if(arr[i-1] == "S" and arr[i] == "F"):
        fs = fs + 1 # from seatle

if(fs>ts):
    print("YES")
else:
    print("NO")