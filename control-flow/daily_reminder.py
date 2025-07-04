# daily_reminder.py

# Prompt for a Single Task:
# Ask the user to input a task description and save it into a task variable.
task = input("Enter your task: ")

# Prompt for the task’s priority (high, medium, low) and save it into a priority variable.
# Convert input to lowercase for easier matching.
priority = input("Priority (high/medium/low): ").lower()

# In a time_bound variable, ask if the task is time-bound (yes or no).
# Convert input to lowercase for easier matching.
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize the final reminder message variable.
final_reminder = ""

# Process the Task Based on Priority and Time Sensitivity:
# Use a Match Case statement to react differently based on the task’s priority.
match priority:
    case 'high':
        # Within the Match Case, use an if statement to modify the reminder if time-bound.
        if time_bound == 'yes':
            # Specific message for high priority, time-bound tasks.
            final_reminder = f"Reminder: '{task}' is a high priority task that requires immediate attention today!"
        elif time_bound == 'no':
            # Default message for high priority, non-time-bound tasks (no specific example given).
            final_reminder = f"Reminder: '{task}' is a high priority task."
        else:
            # Handle invalid time-bound input for high priority.
            print("Invalid time-bound input. Please answer yes or no.")
            exit() # Exit the script if input is invalid
    case 'medium':
        # Default messages for medium priority tasks (no specific examples given).
        if time_bound == 'yes':
            final_reminder = f"Note: '{task}' is a medium priority task and is time-bound."
        elif time_bound == 'no':
            final_reminder = f"Note: '{task}' is a medium priority task."
        else:
            # Handle invalid time-bound input for medium priority.
            print("Invalid time-bound input. Please answer yes or no.")
            exit()
    case 'low':
        # Within the Match Case, use an if statement to modify the reminder if time-bound.
        if time_bound == 'no':
            # Specific message for low priority, non-time-bound tasks.
            final_reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
        elif time_bound == 'yes':
            # Default message for low priority, time-bound tasks (no specific example given).
            final_reminder = f"Note: '{task}' is a low priority task and is time-bound."
        else:
            # Handle invalid time-bound input for low priority.
            print("Invalid time-bound input. Please answer yes or no.")
            exit()
    case _:
        # This is the default case for any invalid priority input.
        print("Invalid priority entered. Please choose high, medium, or low.")
        exit() # Exit the script if input is invalid

# Output the Result:
# Print the customized reminder.
print(final_reminder)