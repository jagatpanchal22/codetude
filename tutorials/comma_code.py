#!/usr/bin/python
"""
Description: Write a function that takes a list value as an argument and returns
a string with all the items separated by a comma and a space, with and inserted before the last item.
"""

def comma_code(listvalue):
    for i in listvalue:
        if listvalue[0] == listvalue[-1]:
            print(i)
        elif i == listvalue[-1]:
            print('and', i)
        else:
            print(i, end=',')

def main():
    """
    A main function which is starting point for program
    :return: None
    """
    print("====== Comma Code Program =====")
    comma_code(['apples', 'bananas', 'tofu', 'cats'])
    comma_code(['apples', 'bananas'])
    comma_code([])
    comma_code([2, 4, 6, 8, 10])
    print("===============================")

if __name__ == "__main__":
    main()
