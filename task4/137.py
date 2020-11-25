def main():

    new_dict = {
        1: ['A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'],
        2: ['D', 'G'],
        3: ['B', 'C', 'M', 'P'],
        4: ['F', 'H', 'W', 'V', 'Y'],
        5: ['K'],
        8: ['J', 'X'],
        10: ['Q', 'Z'],
    }

    s = input()
    s = s.upper()
    cnt = 0

    for i in s:
        for key, value in new_dict.items():
            if i in value:
                cnt += key

    print(cnt)


main()