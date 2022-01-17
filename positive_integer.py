#!/usr/bin/env python3
# Created By: Jedidiah
# Date: Jan 12, 2021
# This program prompts the user to input a positive integer.
# It will then print the multiplication table of that number


def main():
    try:
        user_input = int(input("Enter a whole number: "))
        count = 1
        # we are using while loop for iterating the multiplication 10 times
        print("The Multiplication Table of: ", user_input)
        if user_input <= 0:
            print("Invalid input.")
        else:
            while count <= 10:
                print(user_input, 'x', count, '=', user_input * count)
                count += 1

    except Exception:
        print("Invalid input.")


if __name__ == "__main__":
    main()
