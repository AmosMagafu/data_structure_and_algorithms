def print_right_angle(height):
    for row in range(0, height):
        for col in range(0, row + 1):
            print("*", end="")
        print("")


if __name__ == "__main__":
    height = 5
    print_right_angle(height)
