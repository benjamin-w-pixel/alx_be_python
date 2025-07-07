# temp_conversion_tool.py

# Define Global Conversion Factors:
# At the top of your script, define two global variables
# FAHRENHEIT_TO_CELSIUS_FACTOR and CELSIUS_TO_FAHRENHEIT_FACTOR.
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5 # This line has been re-typed to ensure exact match

# Implement Conversion Functions:
def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius.

    Args:
        fahrenheit (float): The temperature in Fahrenheit.

    Returns:
        float: The temperature converted to Celsius.
    """
    # Formula: (F - 32) * (5/9)
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit.

    Args:
        celsius (float): The temperature in Celsius.

    Returns:
        float: The temperature converted to Fahrenheit.
    """
    # Formula: (C * (9/5)) + 32
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# User Interaction and Main Logic
def main():
    """
    Prompts the user for temperature and unit, performs conversion,
    and displays the result. Handles invalid input.
    """
    try:
        # Prompt the user to enter a temperature.
        temperature_input = input("Enter the temperature to convert: ")
        temperature = float(temperature_input) # Convert to float for calculations
    except ValueError:
        # If conversion to float fails, raise an error as specified.
        print("Invalid temperature. Please enter a numeric value.")
        return # Exit the function if input is invalid

    # Prompt for the unit (C/F).
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    # Based on the user’s input, call the appropriate conversion function.
    if unit == 'F':
        converted_temp = convert_to_celsius(temperature)
        # Display the converted temperature in the specified format.
        print(f"{temperature}°F is {converted_temp}°C")
    elif unit == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        # Display the converted temperature in the specified format.
        print(f"{temperature}°C is {converted_temp}°F")
    else:
        # Handle invalid unit input.
        print("Invalid unit. Please enter 'C' or 'F'.")

if __name__ == "__main__":
    main()