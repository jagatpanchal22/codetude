#!/usr/bin/python
"""
Description: Function for Collatz program   demo purpose
"""
import argparse

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
        parser = argparse.ArgumentParser()
        parser.add_argument("--number")
        args = parser.parse_args()
        userInput = int(args.number)
        res = collatz(userInput)
        print(res)
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    print("============================")


if __name__ == "__main__":
    main()
