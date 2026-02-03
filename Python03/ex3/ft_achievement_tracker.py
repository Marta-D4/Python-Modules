#!/usr/bin/env python3

"""

"""

alice = set(("first_kill", "level_10", "treasure_hunter", "speed_demon"))
bob = set(("first_kill", "level_10", "boss_slayer", "collector"))
charlie = set((
    "level_10", "treasure_hunter", "boss_slayer",
    "speed_demon", "perfectionist"
))

print("=== Achievement Traker System ===\n")
print(f"Player alice achievements: {alice}")
print(f"Player bob achievements: {bob}")
print(f"Player charlie achievements: {charlie}")

print("\n=== Achievement Analytics ===\n")
unique_achieve = alice.union(bob, charlie)
print(f"All unique achievements: {unique_achieve}")
print(f"Total unique achievements: {len(unique_achieve)}")

print(f"\nCommon to all players: {alice.intersection(bob, charlie)}")
# print("Rare achievements")

print(f"\nAlice vs Bob common: {alice.intersection(bob)}")
print(f"Alice unique: {alice.difference(bob)}")
print(f"Bob unique: {bob.difference(alice)}")
