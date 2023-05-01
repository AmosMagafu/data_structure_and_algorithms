def find_first_occurrence(my_list, num):
    for key, value in enumerate(my_list):
        if num == value:
            return key


if __name__ == "__main__":
    integers = [10, 11, 15, 67]
    index_of_integer = find_first_occurrence(integers, 67)
    print("The index of the integer is: ", index_of_integer)
