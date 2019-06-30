#!/usr/bin/env python3
"""
Simple math functions in order to run unit tests against.

The functions here will all take two arguments and perform
some calculation. Intended to showcase unit tests.
"""

def add_it(a, b):
    """Add args a+b"""
    return a + b

def subtract_it(a, b):
    """Subtract args a-b"""
    return a - b

def multiply_it(a, b):
    """Multiply args a*b"""
    return a * b

def main():
    """Calculate some totals"""
    print(f"Adding 2+2 = {add_it(2, 2)} ")
    print(f"Subtracting 5-2 = {subtract_it(5, 2)} ")
    print(f"Multiplying 2x7 = {multiply_it(2, 7)} ")

if __name__ == "__main__":
    main()

