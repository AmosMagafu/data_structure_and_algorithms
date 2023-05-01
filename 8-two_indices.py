def two_indices(nums, target):
    for key1, value1 in enumerate(nums):
        for key2, value2 in enumerate(nums):
            sum = value1 + value2
            if sum == target:
                return [value1, value2]


if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target_sum = 26
    two_integers = two_indices(numbers, target_sum)
    print("Numbers whose sum is {}, are: ".format(target_sum), two_integers)
