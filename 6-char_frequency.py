def character_frequency(string):
    d = dict()
    for char1 in string.lower():
        if char1.isalnum() is True and char1.isdigit() is False:
            f = 0
            for char2 in string.lower():
                if char1 == char2:
                    f = f + 1
            d[char1] = f
    return d


if __name__ == "__main__":
    word = "GROUP NUMBER 8"
    print("The dictionary is: ", character_frequency(word))
