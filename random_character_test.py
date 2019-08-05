#!/usr/bin/env python3
"""Random Character Test"""

# retrieve different types of characters
import string

# Random choice
from random import choice, shuffle

# Get 5 random lowercase letters
string_lowercase = "".join(choice(string.ascii_lowercase) for x in range(5))

# Get 5 random uppercase letters
string_uppercase = "".join(choice(string.ascii_uppercase) for x in range(5))

# Get 5 random punctuation characters
string_punctuation = "".join(choice(string.punctuation) for x in range(5))

# Get 5 random digits
string_digits = "".join(choice(string.digits) for x in range(5))

# Combine all character types
characters = string_lowercase + string_uppercase + string_punctuation + string_digits
print(f"-> Combined charactes: {characters}")

# Turn combined characters into a list and shuffle them
characters_list = list(characters)
shuffle(characters_list)
random_characters = "".join(characters_list)

print(f"-> Characters after shuffle: {random_characters}")
