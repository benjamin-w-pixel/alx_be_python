


try:
    number = int(input("Enter a number to see its multiplication table: "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit() 


print(f"Multiplication table for {number}:") # Optional: a header for clarity
for i in range(1, 11): # Loop from 1 up to (but not including) 11, so 1 to 10
    product = number * i

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