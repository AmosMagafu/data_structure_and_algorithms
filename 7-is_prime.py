def is_prime(number):
    if number > 1:
        for i in range(2, int(number / 2) + 1):
            if (number % i) == 0:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    integer = 4
    print("Is {} prime: ".format(integer), is_prime(integer))
