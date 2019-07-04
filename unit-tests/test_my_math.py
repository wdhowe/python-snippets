#!/usr/bin/env python3
"""
Unit tests for the my_math.py functions.

These unit tests were written for pytest.
Install pytest via pip: pip install pytest
"""

# function to test
import my_math

def test_add_it():
    """Test the my_math add_it function"""
    total = my_math.add_it(5, 2)
    assert total == 7
    assert total > 5
    assert total < 10
    assert type(total) is int

def test_add_it_strings():
    """Test the my_math add_it function with strings"""
    total = my_math.add_it("hello", " world")
    assert total == "hello world"
    assert "hi" not in total
    assert type(total) is str

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

