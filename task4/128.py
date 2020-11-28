def reverselookup(dict, val):
    keys = []
    for k in dict:
        if dict[k] == val:
            keys.append(k)

    return keys

def main():
    test = {"Aron":"true", "apple": "false"}
    print(reverselookup(test, "false"))

    print(reverselookup(test, "1.5"))


main()

