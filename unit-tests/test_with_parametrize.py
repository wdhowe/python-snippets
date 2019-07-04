#!/usr/bin/env python3
"""
Unit tests for the my_math.py functions.

These unit tests were written for pytest.
Install pytest via pip: pip install pytest
"""

# functions to test
import my_math

# in order to decorate with test marking
import pytest

##-- Decorator Explanations --##
# @pytest.mark.parametrize = Create a parametrize list of tests


def test_add_it():
    """Test the my_math add_it function"""
    assert my_math.add_it(5, 2) == 7
    assert my_math.add_it(5, 5) == 10
    assert my_math.add_it("hello", " world") == "hello world"


@pytest.mark.parametrize(
    "arg1, arg2, result", [(5, 2, 7), (5, 5, 10), ("hello", " world", "hello world")]
)
def test_add_it_params(arg1, arg2, result):
    """Test the my_math add_it function with parameters"""
    assert my_math.add_it(arg1, arg2) == result


def main():
    """This is not meant to be executed directly"""
    print("These are unit tests. Execute the tests via pytest.")
    exit(1)


if __name__ == "__main__":
    main()
