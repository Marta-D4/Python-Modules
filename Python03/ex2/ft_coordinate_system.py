#!/usr/bin/env python3

import math

def calc_distance(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    distance = math.sqrt((x2-x1) ** 2 + (y2-y1) ** 2 + (z2-z1) ** 2)
    return f"{distance:.2f}"

def parse_coords(position: str):
    coords = []

    try:
        for num in position.split(','):
            coords.append(int(num))
    except ValueError as error:
        print("Error parsing coordinates: ", error)
        print(f"Error details - Type: ValueError, Args: {error.args}")
        return
    
    if len(coords) != 3:
        print("Number of coordinates expected 3")
        return
    
    return tuple(coords)


print("=== Game Coordinate System ===")

point_start = (10, 20, 5)
point_end = (0, 0, 0)

print(f"\nPosition created: {point_start}")
print(
    f"Distance between {point_end} and {point_start}:"
    f" {calc_distance(point_start, point_end)}"
)

print("\nParsing coordinates: \"3,4,0\"")
point_start = parse_coords("3,4,0")
if point_start:
    print(f"Parsed position: {point_start}")
    print(
        f"Distance between {point_end} and {point_start}:"
        f" {calc_distance(point_start, point_end)}"
    )

print("\nParsing invalid coordinates: \"abc,def,ghi\"")
parse_coords("abc,def,ghi")

print("\nUnpacking demonstration:")
if point_start:
    x, y,z = point_start
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")
