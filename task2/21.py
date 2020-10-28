n = int(input())
str1 = "I love it "
str2 = "I hate it "
str3 = "I love that "
str4 = "I hate that "
res = ""

for i in range(n):

        if(i%2!= 0):
            if(i!=n-1): res+= str3
            else: res += str1


        else:
            if(i!=n-1): res += str4
            else: res+= str2


print(res)