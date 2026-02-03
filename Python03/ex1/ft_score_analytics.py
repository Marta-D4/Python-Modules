#!/usr/bin/env python3

"""
    Processes a list of player scores provided as command-line arguments
"""

import sys

print("=== Player Score Analytics ===")

try:
    # Checks if any scores are provided
    if len(sys.argv) > 1:
        scores = []

        for arg in sys.argv[1:]:
            scores.append(int(arg))

        print(f"Scores processed: {scores}")

        print(f"Total players: {len(scores)}")

        print(f"Total score: {sum(scores)}")

        print(f"Average score: {sum(scores) / len(scores)}")

        print(f"High score: {max(scores)}")

        print(f"Low score: {min(scores)}")

        print(f"Score range: {max(scores)-min(scores)}")
    # Display if no scores are provided
    else:
        print(
            f"No scores provided. Usage: python3 {sys.argv[0]}"
            " <score1> <score2> ..."
        )
# Error handling where the input is not a valid int
except ValueError:
    print(f"ERROR: '{arg}' not valid score value.")
