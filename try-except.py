#!/usr/bin/env python3
"""Showing try,except,finally examples"""

# A number stored as a string
my_number = "123"

try:
    # Attempt to convert to an integer
    my_number = int(my_number)
    print("try: my_number successfully converted to an integer.")
except:
    # If there is an error, display a message and exit
    print("except: my_number is NOT an integer!")
    exit(1)
finally:
    print("finally: I will always be displayed(my_number)\n")

# Store a string
my_number2 = "nope"

try:
    # Attempt to convert to an integer
    my_number2 = int(my_number2)
    print("try: my_number2 successfully converted to an integer.")
except:
    # If there is an error, display a message and exit
    print("except: my_number2 is NOT an integer!")
    print("except: Will exit now.")
    exit(1)
finally:
    print("finally: I will always be displayed(my_number2)")
