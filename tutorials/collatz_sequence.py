def collatz(number):
    """
    A Collatz sequence which checks a number is even or odd returns values according
    :param number: takes an integer value
    :return: returns an integer value
    """
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1


def main():
    """
    A main function which is starting point for program
    :return:
    """
    print("====== Collatz Program =====")
    try:
        userInput = int(input("Enter Value: "))
        res = collatz(userInput)
        print(res)
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    print("============================")


if __name__ == "__main__":
    main()
