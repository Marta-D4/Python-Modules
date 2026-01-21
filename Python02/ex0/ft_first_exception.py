#!/usr/bin/env python3

def check_temperature(temp_str):
    try:
        temp = int(temp_str)
        
        if temp < 0:
            return f"Error: {temp}°C is too cold for plants (min 0°C)"
        elif temp > 40:
            return f"Error: {temp}°C is too hot for plants (max 40°C)"
        else:
            return f"Temperature {temp}°C is perfect for plants!"
        
    except ValueError:
        return f"Error: '{temp_str}' is not a valid number"

def test_temperature_input():
    print("=== Garden Temperature Checker ===")
    
    tests = ["25", "abc", "100", "-50"]
    
    for temp_str in tests:
        print(f"\nTesting temperature: {temp_str}")
        result = check_temperature(temp_str)
        print(result)
    
    print("\nAll tests completed - program didn't crash!")

test_temperature_input()
