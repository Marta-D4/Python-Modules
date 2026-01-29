#!/usr/bin/env python3

def water_plants(plant_list):
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise TypeError(plant)
            print(f"Watering {plant}")

    except TypeError:
        print(f"Error: Cannot water {plant} - invalid plant!")

    else:
        print("Watering completed successfully!")

    finally:
        print("Closing watering system (cleanup)")


# =========================
# Test Function
# =========================

def test_watering_system():
    print("=== Garden Watering System ===")

    print("\nTesting normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])

    print("\nTesting with error...")
    water_plants(["tomato", None, "carrots"])

    print("\nCleanup always happens, even with errors!")


test_watering_system()
