#!/usr/bin/env python3
"""
Open a file and print the contents
Use 'with..as' in order to handle opening/closing the file
and 'for..opened_file' to treat file object as iterable.
This uses memory mgmt and i/o buffering.
"""
from sys import argv

if len(argv) < 2:
    print("> Give me a filename as an argument to print it.")
    exit(1)

THE_FILE = argv[1]

# Open the file and print each line
with open(THE_FILE) as opened_file:
    for line in opened_file:
        print("-> " + line, end="")
