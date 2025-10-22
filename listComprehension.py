"""
Program: List, Set, and Dictionary Comprehension Example
Author: Raphi
Description:
    This program demonstrates how to use list comprehensions (with if/else),
    set comprehensions, and dictionary comprehensions in Python.
    It also shows how to use constants instead of hard-coded numbers.
"""

# Constants
START_NUMBER = 1
END_NUMBER = 10


# Functions
def main():

    # Create a list of numbers from START_NUMBER to END_NUMBER
    numbers = list(range(START_NUMBER, END_NUMBER + 1))

    # List comprehension with if/else:
    # Label each number as "even" or "odd"
    labels = ["even" if n % 2 == 0 else "odd" for n in numbers]
    print("List of even/odd labels:", labels)

    # Set comprehension:
    # Collect all unique consonants (non-vowels) from a word
    word = "programming"
    vowels = "aeiou"
    unique_consonants = {char for char in word if char not in vowels}
    print("Unique consonants in the word:", unique_consonants)

    # Dictionary comprehension:
    # Create a mapping between each number and its square
    squares = {n: n ** 2 for n in numbers}
    print("Dictionary of squares:", squares)


# Program Entry Point
if __name__ == "__main__":
    main()
