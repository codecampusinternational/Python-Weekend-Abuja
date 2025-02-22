# 02-dictionaries.py
# This script demonstrates how to work with dictionaries in Python.

# Example 1: Creating a dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}
print("Person:", person)  # Output: Person: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Example 2: Accessing dictionary values
print("Name:", person["name"])  # Output: Name: Alice

# Example 3: Modifying a dictionary
person["age"] = 26
print("Updated Person:", person)  # Output: Updated Person: {'name': 'Alice', 'age': 26, 'city': 'New York'}

# Activity 1: Dictionary operations
# 1. Create a dictionary for a book with keys `title`, `author`, and `year`.
# 2. Print the author of the book.
# 3. Update the year to 2023.

# Solution:
# book = {"title": "Python Basics", "author": "John Doe", "year": 2020}
# print("Author:", book["author"])  # Output: Author: John Doe
# book["year"] = 2023
# print("Updated Book:", book)  # Output: Updated Book: {'title': 'Python Basics', 'author': 'John Doe', 'year': 2023}