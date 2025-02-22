# 01-errors.py
# This script demonstrates how to handle errors in Python.

# Example 1: TypeError
try:
    result = "10" + 5  # This will cause a TypeError
except TypeError:
    print("Error: Cannot add a string and a number.")  # Output: Error: Cannot add a string and a number.

# Example 2: Handling division by zero
try:
    result = 10 / 0  # This will cause a ZeroDivisionError
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")  # Output: Error: Cannot divide by zero.

# Activity 1: Write a program that asks for a number and handles invalid input.
# Solution:
# try:
#     number = int(input("Enter a number: "))
#     print("You entered:", number)
# except ValueError:
#     print("Invalid input! Please enter a number.")