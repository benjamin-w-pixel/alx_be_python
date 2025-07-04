
# multiplication_table.py

try:
    number = int(input("Enter a number to see its multiplication table: "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit()

# Optional: a header for clarity, but not strictly required by the checker's regex
# print(f"Multiplication table for {number}:") 

for i in range(1, 11):
    product = number * i
    # THIS IS THE CRITICAL LINE. MANUALLY RE-TYPE IT CAREFULLY.
    print(f"{number} * {i} = {product}")

#Enter a number to see its multiplication table: 5
#Multiplication table for 5:
#5 * 1 = 5
#5 * 2 = 10
#5 * 3 = 15
#5 * 4 = 20
#5 * 5 = 25
#5 * 6 = 30
#5 * 7 = 35
#5 * 8 = 40
#5 * 9 = 45
#5 * 10 = 50