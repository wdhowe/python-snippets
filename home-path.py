#!/usr/bin/env python3
"""Display user's home path"""

# OS Module
import os

# Get user's home path
user_home = os.environ.get("HOME")

print("Home path is: " + user_home)
