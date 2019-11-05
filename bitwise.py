#!/usr/bin/env python3
"""Bitwise Operators Examples"""


def main():
    """Display bitwise examples"""
    bit_a = 60
    bit_b = 13
    print(f"Bitwise operators")
    print(f"Example values: bit_a = {bin(bit_a)}, bit_b = {bin(bit_b)}")

    print(f"\n& (binary AND, copies a bit if it exists in both): {bin(bit_a & bit_b)}")

    print(f"\n| (binary OR, copies a bit if it exists in either): {bin(bit_a | bit_b)}")

    print(f"\n~ (binary ones complement, flips the bits): for bit_a: {bin(~bit_a)}")

    print(
        f"\n<< (binary shift left, left side moved by num of bits on the right side): for bit_a << 2: {bin(bit_a << 2)}"
    )

    print(
        f"\n>> (binary shift right, left side moved by num of bits on the right side): for bit_a >> 2: {bin(bit_a >> 2)}"
    )


if __name__ == "__main__":
    main()
