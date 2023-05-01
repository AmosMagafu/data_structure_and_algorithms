def int_to_roman(n):
    nums = [1, 4, 5, 9, 10, 40, 50, 90,
            100, 400, 500, 900, 1000]
    syms = ["I", "IV", "V", "IX", "X", "XL",
            "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
    answer = ""
    while n:
        q = n // nums[i]
        n = n % nums[i]
        while q:
            answer = answer + syms[i]
            q = q - 1
        i = i - 1
    return answer


if __name__ == "__main__":
    number = 5438
    print("{} to roman is: ".format(number), int_to_roman(number))
