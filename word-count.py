#!/usr/bin/env python3
"""
word-count.py snippet
Count occurences of words in a list.
"""

word_list = ["one", "two", "three", "two", "three", "three"]
word_counts = {}

for word in word_list:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(f"-> Original List: {word_list}")
print(f"\n-> Counted words: {word_counts}")
