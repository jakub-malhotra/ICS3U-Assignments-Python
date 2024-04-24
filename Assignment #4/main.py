#!/usr/bin/env python3
"""
Created by: Jakub Malhotra
Created on: April 2024
This is the "weekday" module
"""


def main() -> None:
    """This is the main function."""

    # Input
    user_input_as_string = input(
        "Enter a number 1-7 to see the corresponding day of the week: "
    )

    # Process and Output
    try:
        user_input_as_number = int(user_input_as_string)
    except ValueError:
        print(f"The error was {ValueError}.")
    else:
        if user_input_as_number <= 0 or user_input_as_number > 7:
            print("Please enter a valid day of the week.")
        else:
            match user_input_as_number:
                case 1:
                    print("Sunday")
                case 2:
                    print("Monday")
                case 3:
                    print("Tuesday")
                case 4:
                    print("Wednesday")
                case 5:
                    print("Thursday")
                case 6:
                    print("Friday")
                case 7:
                    print("Saturday")
                case _:
                    print("Error.")
    finally:
        print("")

    print("Done.")


if __name__ == "__main__":
    main()
