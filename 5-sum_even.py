def sum_even_numbers(my_list):
    s = 0
    for key, value in enumerate(my_list):
        if(value % 2 == 0):
            s = s + my_list[key]
    return s


if __name__ == "__main__":
    integers = [33, 34, 53, 54, 73, 74]
    total = sum_even_numbers(integers)
    print("Sum of even numbers from the list is: ", total)
