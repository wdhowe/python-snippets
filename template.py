#!/usr/bin/env python3
"""
Title:
Description:
Author:
"""

# =======================
# Import Modules
# =======================
# argparse: Command line arguments
import argparse

# =======================
# Functions; main after
# =======================
def get_arguments():
    """Build argument parser information."""
    parser = argparse.ArgumentParser(description="Put a good program description here.")
    parser.add_argument(
        "-n", "--name", help="This is your name.[Required]", required=True
    )
    parser.add_argument(
        "-e", "--email", help="Email results.", action="store_true", required=False
    )
    parser.add_argument(
        "-t",
        "--test",
        help="Do not make changes; perform a test and output details of what would happen.",
        action="store_true",
        required=False,
    )
    args = vars(parser.parse_args())

    return args


def another_fuction(args):
    """Display some things."""
    print(f"> Hello, {args['name']}!")

    return


# =======================
# Main Program Control
# =======================
def main():
    """Get some arguments and display things."""
    args = get_arguments()
    if args["test"] == True:
        print("-->> Test run...no modifications will be made <<--")

    another_fuction(args)

    return 0


# =======================
# Execute Main Program
# =======================
if __name__ == "__main__":
    main()
