#!/usr/bin/env python3

# =========================
# Temperature checking function
# =========================

def check_temperature(temp_str):
    """
    Checks if temperature is valid for plants.
    Input validation and ValueError handling.
    """
    try:
        temp = int(temp_str)

        if temp < 0:
            return f"Error: {temp}°C is too cold for plants (min 0°C)"
        elif temp > 40:
            return f"Error: {temp}°C is too hot for plants (max 40°C)"
        else:
            return f"Temperature {temp}°C is perfect for plants!"

    # Runs if int cast fails
    except ValueError:
        return f"Error: '{temp_str}' is not a valid number"


# =========================
# Test Function
# =========================

def test_temperature_input():
    print("=== Garden Temperature Checker ===")

    # Test inputs (valid int, invalid str, too hot, too cold)
    tests = ["25", "abc", "100", "-50"]

    # Checks each temperature input
    for temp_str in tests:
        print(f"\nTesting temperature: {temp_str}")
        result = check_temperature(temp_str)
        print(result)

    print("\nAll tests completed - program didn't crash!")


test_temperature_input()
