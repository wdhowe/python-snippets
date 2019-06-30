#!/usr/bin/env python3
"""
Unit tests for the my_math.py functions.

These unit tests were written for pytest.
Install pytest via pip: pip install pytest
"""

import my_math

def test_add_it():
    """Test the my_math add_it function"""
    total = my_math.add_it(5, 2)
    assert total == 7

def test_subtract_it():
    """Test the my_math subtract_it function"""
    total = my_math.subtract_it(5, 2)
    assert total == 3

def test_multiply_it():
    """Test the my_math multiply_it function"""
    total = my_math.multiply_it(5, 2)
    assert total == 10

def main():
    """This is not meant to be executed directly"""
    print("These are unit tests. Execute the tests via pytest.")
    exit(1)

if __name__ == "__main__":
    main()

