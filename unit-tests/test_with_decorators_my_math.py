#!/usr/bin/env python3
"""
Unit tests for the my_math.py functions.

These unit tests were written for pytest.
Install pytest via pip: pip install pytest
"""

# function to test
import my_math

# in order to decorate with test marking
import pytest

# for sys call of version_info in decorator
import sys

##-- Decorator Explanations --##
# @pytest.mark.groupA or groupB = custom decorator marks for test filtering
# @pytest.mark.skip("Do not run this test for now.") = test will be skipped
# @pytest.mark.skipif(
#    sys.version_info < (3, 0), reason="Do not run this test if python version is < 3.0"
# ) = test will be skipped if condition is met


@pytest.mark.groupA
def test_add_it():
    """Test the my_math add_it function"""
    total = my_math.add_it(5, 2)
    assert total == 7
    assert total > 5
    assert total < 10
    assert type(total) is int


@pytest.mark.groupB
def test_add_it_strings():
    """Test the my_math add_it function with strings"""
    total = my_math.add_it("hello", " world")
    assert total == "hello world"
    assert "hi" not in total
    assert type(total) is str


@pytest.mark.groupA
@pytest.mark.skip("Do not run this test for now.")
def test_subtract_it():
    """Test the my_math subtract_it function"""
    total = my_math.subtract_it(5, 2)
    assert total == 3


@pytest.mark.groupB
@pytest.mark.skipif(
    sys.version_info < (3, 0), reason="Do not run this test if python version is < 3.0"
)
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
