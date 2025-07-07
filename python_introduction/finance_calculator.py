# finance_calculator.py

# User Input for Financial Details:
# Prompt the user for their monthly income.
try:
    monthly_income = float(input("Enter your monthly income: "))
except ValueError:
    print("Invalid input for monthly income. Please enter a valid number.")
    exit() # Exit the script if input is not a valid number

# Ask for their total monthly expenses.
try:
    monthly_expenses = float(input("Enter your total monthly expenses: "))
except ValueError:
    print("Invalid input for monthly expenses. Please enter a valid number.")
    exit() # Exit the script if input is not a valid number

# Calculate Monthly Savings:
# Calculate the monthly savings by subtracting monthly expenses from the monthly income.
monthly_savings = monthly_income - monthly_expenses

# Project Annual Savings:
# Assume a simple annual interest rate of 5%.
annual_interest_rate = 0.05

# Calculate the projected savings after one year, incorporating the interest.
# Use the simplified formula: (Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05)).
projected_annual_savings = (monthly_savings * 12) + (monthly_savings * 12 * annual_interest_rate)

# Output Results:
# Display the user’s monthly savings.
print(f"Your monthly savings are ${monthly_savings:.2f}.") # .2f for 2 decimal places

# Display the projected annual savings after including interest.
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings:.2f}.") # .2f for 2 decimal places