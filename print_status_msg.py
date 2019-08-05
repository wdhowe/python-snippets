#!/usr/bin/env python3
"""Displaying status messages by flushing the print buffer"""

# =======================
# Import Modules
# =======================
# Future print function capabilities
from __future__ import print_function

# sys: for stdout print buffer flush
import sys

# time: for sleeping
import time

# -- Example status message code --#
print("Doing some work", end="")

# Loop from 0 to 9
for count in range(9):

    # Print a period '.' with no newline
    print(".", end="")

    # Flush the stdout buffer to display it immediately to the console
    sys.stdout.flush()

    # sleep for 1 second
    time.sleep(1)

print("[COMPLETE]")
