#!/usr/bin/env python3
"""Named Tuples Example"""

from collections import namedtuple


def main():
    """Show some cat tuples"""
    Cat = namedtuple("Cat", ("name", "age", "color"))

    cat01 = Cat("Robert", "10", "black/white")
    cat02 = Cat("Jones", "1", "spotted")

    print(f"Cats are:")
    print(f"{cat01.name} - {cat01.age} - {cat01.color}")
    print(f"{cat02.name} - {cat02.age} - {cat02.color}")


if __name__ == "__main__":
    main()
