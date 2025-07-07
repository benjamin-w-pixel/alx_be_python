# arithmetic_operations.py

# Define a function named perform_operation.
# Parameters: num1 (float), num2 (float), and operation (string).
# The operation parameter accepts 'add', 'subtract', 'multiply', or 'divide'.
def perform_operation(num1, num2, operation):
    """
    Performs basic arithmetic operations based on the given numbers and operation.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').

    Returns:
        float or str: The result of the operation, or an error message for division by zero.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        # Handle division by zero.
        if num2 == 0:
            return "Cannot divide by zero." # Return specific message as required
        else:
            return num1 / num2
    else:
        # Handle invalid operation input (though main.py should prevent this by stripping/lowering)
        return "Invalid operation."

# This script only defines the function. It does not call it directly,
# as it's meant to be imported by main.py.