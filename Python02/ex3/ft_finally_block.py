#!/usr/bin/env python3

def water_plants(plant_list):
    """
    Watering system for a list of plants
    try / except / else / finally behavior
    """
    print("Opening watering system")
    # Waters plant if its valid, raises error if not
    try:
        for plant in plant_list:
            if plant is None:
                raise TypeError(plant)
            print(f"Watering {plant}")

    # Catches TypeError raised
    except TypeError:
        print(f"Error: Cannot water {plant} - invalid plant!")

    # Only runs if NO exceptions ocurred
    else:
        print("Watering completed successfully!")

    # Always runs, with or without errors
    finally:
        print("Closing watering system (cleanup)")


# =========================
# Test Function
# =========================

def test_watering_system():
    print("=== Garden Watering System ===")

    # Case with all valid plants
    print("\nTesting normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])

    # Case with invalid type (None)
    print("\nTesting with error...")
    water_plants(["tomato", None, "carrots"])

    print("\nCleanup always happens, even with errors!")


test_watering_system()
