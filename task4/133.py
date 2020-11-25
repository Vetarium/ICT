user_in = input()
dict = {
  "A": "Newfoundland",
  "B": "Nove Scotia",
  "C": "Prince Edward Island",
  "E": "New Brunswik",
  "G": "Quebec",
  "H": "Quebec",
  "J": "Quebec",
  "K": "Ontario",
  "L": "Ontario",
  "M": "Ontario",
  "N": "Ontario",
  "P": "Ontario",
  "R": "Manitoba",
  "S": "Saskatchewan",
  "T": "Alberta",
  "V": "British Columbia",
  "X": "Northwestern territories/Nunavut",
  "Y": "Yukon",
  "1": "urban",
  "2": "urban",
  "3": "urban",
  "4": "urban",
  "5": "urban",
  "6": "urban",
  "7": "urban",
  "8": "urban",
  "9": "urban",
  "0": "rural",
}
ans = ""
for x in range(0,2):
    ans=ans+(dict[user_in[x]])+" "
print(ans)