user_input = input()

u = {
  "1": "one",
  "2": "two",
  "3": "three",
  "4": "four",
  "5": "five",
  "6": "six",
  "7": "seven",
  "8": "eight",
  "9": "nine"
}

d = {
  "1": "ten",
  "2": "twenty",
  "3": "thirty",
  "4": "forty",
  "5": "fifty",
  "6": "sixty",
  "7": "seventy",
  "8": "eighty",
  "9": "ninety"
}

d_ = {
  "1": "eleven",
  "2": "twelve",
  "3": "thirteen",
  "4": "forteen",
  "5": "fifteen",
  "6": "sixteen",
  "7": "seventeen",
  "8": "eighteen",
  "9": "nineteen"
}


h = {
  "1": "one hundred",
  "2": "two hundred",
  "3": "three hundred",
  "4": "four hundred",
  "5": "five hundred",
  "6": "six hundred",
  "7": "seven hundred",
  "8": "eight hundred",
  "9": "nine hundred"
}





def print_number(user_input):
    s = ""
    if(len(user_input)==3):
        s = s + h[user_input[0]] + " "
        user_input = int(user_input)
        if(user_input%100>10 and user_input%100<=19):
            s = s + d_[str(user_input%10)]
            print(s)
            exit()
        user_input = str(user_input)
        s = s + d[user_input[1]] + " "
        s = s + u[user_input[2]] + " "
    if(len(user_input)==2):
        user_input = int(user_input)
        if(user_input%100>10 and user_input%100<19):
            s = s + d_[str(user_input%10)]
            print(s)
            exit()
        user_input = str(user_input)
        s = s + d[user_input[0]] + " "
        s = s + u[user_input[1]] + " "
    if(len(user_input)==1):
        s = s + u[user_input[0]] + " "
    print(s)

print_number(user_input)