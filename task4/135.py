#anagrams

def cntr(s):
    counts = {}
    for c in s:
        if c in counts:
            counts[c] = counts[c]+1
        else:
            counts[c]=1
    return counts

def main():

    str1 = input()
    str2 = input()

    res1 = cntr(str1)
    res2 = cntr(str2)

    if res1 == res2:
        print("anagrams")
    else:
        print("not anagrams")



main()