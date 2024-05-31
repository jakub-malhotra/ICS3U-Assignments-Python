#!/usr/bin/env python3
"""
Created by: Jakub Malhotra
Created on: May 2024
This module computes the sum of a list.
"""


from typing import List


def calculate_sum(list_of_numbers: List[float]) -> float:
    """Calculates the sum  of the values in the given list."""
    total = 0
    for number in list_of_numbers:
        total += number

    # round the sum to 2 decimal places
    sum_rounded = round(total, 2)

    return sum_rounded


def main() -> None:
    """Main function calls the sum calculator function."""
    list_of_numbers = []

    print("Enter 'stop' to stop entering numbers")

    # loop to get numbers from user
    while True:
        temporary_input_as_string = input(
            "What is the number you wish to add to the list: "
        )
        if temporary_input_as_string == "stop":
            break
        try:
            temporary_input = float(temporary_input_as_string)
        except ValueError:
            print("Only enter numbers or 'stop'.")
        else:
            list_of_numbers.append(temporary_input)

    # Process: Find the total of the list
    sum_rounded = calculate_sum(list_of_numbers)

    # Output: Display the largest value
    print(f"The sum is {sum_rounded}")

    print("\nDone.")


if __name__ == "__main__":
    main()
