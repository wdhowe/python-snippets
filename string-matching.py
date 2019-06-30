#!/usr/bin/env python3
"""Test some string manipulation"""

# strings for testing
my_string1 = "Red Hat Linux"
my_string2 = "CentOS"
my_string3 = "Debian"
my_string4 = "Ubuntu Linux"

my_string_list = [my_string1, my_string2, my_string3, my_string4]

for string in my_string_list:

    # Starts with matching
    if string.startswith("C"):
        print(string + " matched a 'C' begining.")

    # Matching slice: character at index 1 up to, but not including index 2
    #    string indexes start at 0 = the 2nd character in the string.
    if string.startswith("e", 1, 2):
        print(string + " matched a 'e' in the 2nd character.")

    # Ends with matching
    if string.endswith("Linux"):
        print(string + " matched a 'Linux' at the end.")

    # Find a string within a string (returns -1 if not found)
    if string.find("Hat") != -1:
        print("Found 'Hat' in string: " + string)
