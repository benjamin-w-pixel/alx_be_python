try:
    size = int(input("Enter the size of the pattern: "))
    # Ensure the input is a positive integer
    if size <= 0:
        print("Please enter a positive integer for the pattern size.")
        exit()
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit() # Exit the script if the input is not a valid integer

# Draw the Pattern:
# Use a while loop to iterate through each row of the pattern.
row_count = 0
while row_count < size:
    # Inside the while loop, use a for loop to print asterisks (*) side by side.
    # Use print("*", end="") to prevent a new line after each asterisk.
    for _ in range(size): # The underscore '_' is used as a throwaway variable
        print("*", end="")
    
    # After completing each row, print a newline character to move to the next row.
    print() # This print() with no arguments prints a newline

    # Increment the row_count to move to the next row in the while loop
    row_count += 1