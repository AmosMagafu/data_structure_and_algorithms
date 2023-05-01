def factorize(number):
    prime_factors = []
    prime_factor = 2
    while(number > 1):
        if(number % prime_factor == 0):
            prime_factors.append(prime_factor)
            number = number / prime_factor
        else:
            prime_factor = prime_factor + 1
    return prime_factors


if __name__ == "__main__":
    integer = 753
    print("The prime factors of {} is: ".format(integer), factorize(integer))
