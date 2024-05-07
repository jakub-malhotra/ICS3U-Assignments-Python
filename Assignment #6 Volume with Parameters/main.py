#!/usr/bin/env python3
"""
Created by: Jakub Malhotra
Created on: April 2024
This is the "Calculate volume of a rectangular prism" module
"""


def calculate_volume(
    length_as_number: float, width_as_number: float, height_as_number: float
) -> float:
    """This is the calculate volume function"""

    # process
    volume = length_as_number * width_as_number * height_as_number

    volume_rounded = round(volume, 2)

    return volume_rounded


def main() -> None:
    """This is the main function. it calls the volume function"""

    volume_rounded = 0

    # input
    length_as_string = input("Enter the length of the rectangular prism (cm): ")
    width_as_string = input("Enter the width of the rectangular prism (cm): ")
    height_as_string = input("Enter the height of the rectangular prism (cm): ")

    try:
        length_as_number = float(length_as_string)
        width_as_number = float(width_as_string)
        height_as_number = float(height_as_string)
    except ValueError:
        print(f"\nThe error was {ValueError}.")
    else:
        if (length_as_number <= 0) or width_as_number <= 0 or (height_as_number <= 0):
            print("\nSorry only positive numbers can be used for this calculation.")
        else:
            # call function
            volume_rounded = calculate_volume(
                length_as_number, width_as_number, height_as_number
            )
            # output
            print(f"\nThe volume of the rectangular prism is {volume_rounded} cm³.")

    print("\nDone.")


if __name__ == "__main__":
    main()
