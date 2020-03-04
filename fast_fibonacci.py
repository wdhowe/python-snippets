#!/usr/bin/env python3

"""
Using memoization to speed up fibonacci calculations.
Records computed fib values in a dictionary to prevent duplicate compute time
"""


def fib_memo(num, memo=None):
    """
    Assume num >= 0
    memo is a dictionary used to prevent duplicate calcuations
    """

    if memo is None:
        # dictionary not created yet
        memo = {}
    if num == 0 or num == 1:
        # fibonacci base case
        return 1
    try:
        # attempt to lookup the result
        return memo[num]
    except KeyError:
        # result not caculated yet, perform calculation
        result = fib_memo(num - 1, memo) + fib_memo(num - 2, memo)
        # store result in dictionary
        memo[num] = result
        return result


print(f"-> Fib of 5 is: {str(fib_memo(5))}")
print(f"-> Fib of 100 is: {str(fib_memo(100))}")
