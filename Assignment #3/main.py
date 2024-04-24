#!/usr/bin/env python3
"""
Created by: Jakub Malhotra
Created on: March 2024
This is the "number comparison" module
"""


def main() -> None:
    """This is the main function. it compares the values of two numbers"""
    # input
    print("Enter two numbers you want to compare values of. ")
    number_one = int(input("Enter the first number: "))
    number_two = int(input("Enter the second number: "))

    # process
    if number_one > number_two:
        # output
        print(f"{number_one} > {number_two}")
    elif number_one < number_two:
        # output
        print(f"{number_one} < {number_two}")
    else:
        # output
        print(f"{number_one} = {number_two}")

    print("\nDone.")


if __name__ == "__main__":
    main()
