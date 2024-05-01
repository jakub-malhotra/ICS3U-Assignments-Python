#!/usr/bin/env python3
"""
Created by: Jakub Malhotra
Created on: April 2024
This is the "Fibonacci" module
"""


def main() -> None:
    """This is the main function."""

    # Input
    user_input_as_string = input(
        "Enter how many numbers of the Fibonacci sequence should be printed: "
    )

    # Process and Output
    try:
        user_input_as_number = int(user_input_as_string)
    except ValueError:
        print(f"The error was {ValueError}.")
    else:
        if user_input_as_number <= 0:
            print("Please enter a positive number")
        else:
            # set the first two numbers of the sequence
            previous_number, current_number = 0, 1
            # set the counter
            counter = 0
            while counter < user_input_as_number:
                print(f"Term {counter} is {previous_number}")
                # set the next number using the Fibonacci formula
                next_number = previous_number + current_number
                # update the numbers to make the program loop
                previous_number = current_number
                current_number = next_number
                counter += 1

    finally:
        print("")

    print("Done.")


if __name__ == "__main__":
    main()
