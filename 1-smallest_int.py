def get_smallest_integer(my_list):
    small_num = my_list[0]
    for integer in my_list:
        if small_num > integer:
            small_num = integer
    return small_num


if __name__ == "__main__":
    integers = [10, 55, 46, 78, 127]
    smallest_integer = get_smallest_integer(integers)
    print("The smallest integer is: ", smallest_integer)
