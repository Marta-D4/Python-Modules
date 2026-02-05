#!/usr/bin/env python3

"""
    Game Analytics Dashboard using List, Dict, and Set Comprehensions.
    Provides insights into players' scores, achievements, and more.
"""

# Datos de jugadores con logros en sets
players = {
    'alice': {
        'total_score': 2824,
        'favorite_mode': 'ranked',
        'achievements': set((
            "first kill", "treasure_hunter",
            "level_10", "speed_demon"
        ))
    },
    'bob': {
        'total_score': 465,
        'favorite_mode': 'ranked',
        'achievements': set((
            "first kill",
            "boss_slayer", "collector"
        ))
    },
    'charlie': {
        'total_score': 9935,
        'favorite_mode': 'casual',
        'achievements': set((
            "first kill",
        ))
    },
    'diana': {
        'total_score': 3100,
        'favorite_mode': 'ranked',
        'achievements': set((
            "speed_demon", "boss_slayer", "level_10"
        ))
    }
}

# =========================
# Main program execution
# =========================

print("=== Game Analytics Dashboard ===\n")

# Players with +2000 score
high_scorers = [player for player, data in players.items() if data['total_score'] > 2000]

# List of doubled scores
doubled_scores = [data['total_score'] * 2 for data in players.values()]

# Active players (+1 achievements)
active_players = [player for player, data in players.items() if len(data['achievements']) > 1]

print("\n=== List Comprehension Examples ===")
print(f"High scorers (>2000): {high_scorers}")
print(f"Scores doubled: {doubled_scores}")
print(f"Active players (more than 1 achievement): {active_players}")


# Dict with players scores
player_scores = {player: data['total_score'] for player, data in players.items()}

# Types of scores
score_categories = {
    player: 'high' if data['total_score'] > 2000 else 'low'
    for player, data in players.items()
}

# Count each players achievements
achievement_counts = {player: len(data['achievements']) for player, data in players.items()}

print("\n=== Dict Comprehension Examples ===")
print(f"Player scores: {player_scores}")
print(f"Score categories: {score_categories}")
print(f"Achievement counts: {achievement_counts}")


# Unique players
unique_players = {player for player in players}

# Unique achievements
unique_achievements = {achievement for data in players.values() for achievement in data['achievements']}

# Unique modes
unique_modes = {data['favorite_mode'] for data in players.values()}

print("\n=== Set Comprehension Examples ===")
print(f"Unique players: {unique_players}")
print(f"Unique achievements: {unique_achievements}")
print(f"Unique modes: {unique_modes}")


# Total players
total_players = len(players)

# Total unique achievements
total_unique_achievements = len(unique_achievements)

# Average score
average_score = sum(data['total_score'] for data in players.values()) / total_players

# Top player
top_performer = max(players.items(), key=lambda x: x[1]['total_score'])

print("\n=== Combined Analysis ===")
print(f"Total players: {total_players}")
print(f"Total unique achievements: {total_unique_achievements}")
print(f"Average score: {average_score}")
print(f"Top performer: {top_performer[0]} ({top_performer[1]['total_score']} points, {achievement_counts[top_performer[0]]} achievements)")
