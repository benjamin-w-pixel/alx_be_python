# match_case_calculator.py

# Step 1: Prompt for User Input
# Ask the user to input the first number and convert it to a float
try:
    num1 = float(input("Enter the first number: "))
except ValueError:
    print("Invalid input for the first number. Please enter a valid number.")
    exit() # Exit the script if the input is not a valid number

# Ask the user to input the second number and convert it to a float
try:
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Invalid input for the second number. Please enter a valid number.")
    exit() # Exit the script if the input is not a valid number

# Ask for the type of operation
operation = input("Choose the operation (+, -, *, /): ")

# Step 2: Perform the Calculation Using Match Case
# Step 3: Output the Result (and handle division by zero)
match operation:
    case '+':
        result = num1 + num2
        print(f"The result is {result}.")
    case '-':
        result = num1 - num2
        print(f"The result is {result}.")
    case '*':
        result = num1 * num2
        print(f"The result is {result}.")
    case '/':
        # Handle division by zero case gracefully
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}.")
    case _: # This is the default case for any other input
        print("Invalid operation. Please choose from +, -, *, /.")