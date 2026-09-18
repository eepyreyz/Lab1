# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Rey Abbas
# Date: 2026/09/18
# Purpose: Use arithmetic in python.
# Usage: ./lab1b.py

# TO-DO 1:
#	Create a variable called "num1", take its value from user.
num1 = input("Enter the first value: ")

#	Create another variable called "num2" and take its value from user. 
num2 = input("Enter the second value: ")

# Convert the values to integers using int() function
num1 = int(num1)

print(f"\nValue 1 is: {num1}")

num2 = int(num2)
print(f"Value 2 is: {num2}")

# TO-DO 2:
# Perform all arithmetic oeprations as outlined in the description in README.md file, and print in the required format.
print(f"\nnum1 + num2 = {num1 + num2}")
print(f"num1 - num2 = {num1 - num2}")
print(f"num1 * num2 = {num1 * num2}")
print(f"num1 ** num2 = {num1 ** num2}")
print(f"num1 / num2 = {num1 / num2}")
print(f"num1 // num2 = {num1 // num2}")
print(f"num1 % num2 = {num1 % num2}")

