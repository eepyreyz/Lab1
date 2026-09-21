
# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:Rey Abbas
# Date: 2026/09/21
# Purpose: Use string methods and f-string formating.
# Usage: ./lab1c.py

#TO-DO 1:
# import math module.
import math
# Create a variable called 'radius' and take its value form user.
radius = input("What is the radius? ")
# Convert the variable to integer using int()
radius = int(radius)
# use the contant pi form math module and compute the area of the circle using the variable 'radius'
area = math.pi * (radius ** 2)
print(f'The circle area is: {area}')