# explore_datetime.py

# Import necessary components from the datetime module
from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    """
    Obtains and prints the current date and time in "YYYY-MM-DD HH:MM:SS" format.
    """
    # Get the current date and time
    current_date = datetime.now()

    # Format and print the current date and time
    # strftime("%Y-%m-%d %H:%M:%S") ensures the specified format
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

# Part 2: Calculate a Future Date
def calculate_future_date():
    """
    Prompts the user for a number of days, calculates a future date,
    and prints it in "YYYY-MM-DD" format.
    """
    try:
        # Prompt the user to enter a number of days (as an integer).
        num_days = int(input("Enter the number of days to add to the current date: "))
    except ValueError:
        print("Invalid input. Please enter a whole number for the number of days.")
        return # Exit the function if input is not a valid integer

    # Get the current date again (or pass it from display_current_datetime if desired)
    # For simplicity and adherence to the prompt structure, we get it again.
    current_date_for_calc = datetime.now()

    # Calculate what the date will be after adding the specified number of days.
    # Use timedelta(days=number_of_days) to represent the duration.
    future_date = current_date_for_calc + timedelta(days=num_days)

    # Print the future date in a format like “YYYY-MM-DD”.
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

# Main execution block
if __name__ == "__main__":
    # Call the function to display current date and time
    display_current_datetime()

    # Call the function to calculate and display a future date
    calculate_future_date()