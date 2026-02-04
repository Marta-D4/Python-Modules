#!/usr/bin/env python3

print("=== Player Inventory System ===")

players = {
    'alice': {
        'sword': {
            'type': 'weapon',
            'rarity': 'rare',
            'quantity': 1,
            'value': 500
        },
        'potion': {
            'type': 'consumable',
            'rarity': 'common',
            'quantity': 5,
            'value': 50
        },
        'shield': {
            'type': 'armor',
            'rarity': 'uncommon',
            'quantity': 1,
            'value': 200
        }
    },
    'bob': {}
}

for key, value in players.items():
    print(f"Key: {key}, Value: {value}")
