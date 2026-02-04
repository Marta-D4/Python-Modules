#!/usr/bin/env python3

"""
    Allows players to analyze and compare their achievements through sets (unordered collection 
    of unique elements).
    Set operations such as 'union()'"|", 'intersection()'"&", and 'difference()'"-"
    will be used.
"""

alice = set(("first_kill", "level_10", "treasure_hunter", "speed_demon"))
bob = set(("first_kill", "level_10", "boss_slayer", "collector"))
charlie = set((
    "level_10", "treasure_hunter", "boss_slayer",
    "speed_demon", "perfectionist"
))

# =========================
# Main program execution
# =========================

print("=== Achievement Traker System ===\n")

# Displays all achievements of each player
print(f"Player alice achievements: {alice}")
print(f"Player bob achievements: {bob}")
print(f"Player charlie achievements: {charlie}")

print("\n=== Achievement Analytics ===\n")

# Displays all available achievements and their total
all_achievements = alice.union(bob, charlie)
print(f"All unique achievements: {all_achievements}")
print(f"Total unique achievements: {len(all_achievements)}")

# Displays the achievements that only one player has (rare)
print(f"\nCommon to all players: {alice.intersection(bob, charlie)}")
rare_achievements = all_achievements - (
    alice.intersection(bob) | alice.intersection(charlie) | bob.intersection(charlie)
)
print(f"Rare achievements (1 player): {rare_achievements}")

# Displays the comparison between alice and bobs achievements
print(f"\nAlice vs Bob common: {alice.intersection(bob)}")
print(f"Alice unique: {alice.difference(bob)}")
print(f"Bob unique: {bob.difference(alice)}")
