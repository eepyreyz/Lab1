
# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Rey Abbas
# Date: 2026/09/21
# Purpose: Use string methods and f-string formating.
# Usage: ./lab1c.py

#TO-DO 1:
# Create a variable called "quantity".
# The value of "quantity" should be a decimal number of your own choice.
quantity = 6.7
# Create another variable called "stock"
# The value of "stock" should also be a decimal number of your own choice.
stock = 7.6
# Print the product of `quantity` and `stock` with 4 spaces before the answer using the module % formatting.
print("    %f" % (quantity * stock))


# Then print the product of `quantity` and `stock` with 7 spaces before the answer and make sure the answer only goes to hundreadths (-.--) using the module % formatting.
print("       %.2f" % (quantity * stock))
