
# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Rey Abbas
# Date: 2026/09/21
# Purpose: Use string methods and f-string formating.
# Usage: ./lab1d.py

#TO-DO 1:
#	Create a variable called "name" and assign it the value of your name.
name = "Rey"
# Use the string method .upper() to convert the name to upper case.
name = name.upper()
# Create another variable called “age”, the value of “age” should be your age
age = 18
# The script, when executed, should print out "How are you yourname? Happy xxth birthday!" To print this output use .format() method. 
print("How are you {}? \nHappy {}th birthday!".format(name, age))

#TO-DO 2:
# Create a variable called "words".
# The value of words should be "The quick brown fox jumps over the lazy dog".
words = "The quick brown fox jumps over the lazy dog"
# Use indexing to return the first and 17th charecters of "words" to the user.
print(words[0],words[16])

#TO-DO 3:
# Use negative indexing to return the words "jumps" and "quick" from "words" to the user.
print(words[-23:-18],words[-39:-34])

#TO-DO 4:
# Use slicing to retun everything between index 2-15 to the user.
print(words[2:16])

# Print "uick brown foxs ju" from "words". 

# There is an s after the word fox, which there isnt on the origial word
# I wouldve done this print(words[5:22]) if there wasnt

firstHalf = words[5:19]
secondHalf = words[20:22]
print(f'{firstHalf}s {secondHalf}')
