#!/usr/bin/env python3

"""Exploring receiving arguments from the user"""

import sys

print("=== Command Quest ===")

# Displays all arguments received
if len(sys.argv) > 1:
    print(f"Program name: {sys.argv[0]}")
    print(f"Arguments received: {len(sys.argv)-1}")

    # Enumerates each argument
    i = 1
    for arg in sys.argv[1:]:
        print(f"Argument {i}: {arg}")
        i += 1
# In case there were no arguments provided
else:
    print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")

# Displays the total number of arguments
print(f"Total arguments: {len(sys.argv)}")
