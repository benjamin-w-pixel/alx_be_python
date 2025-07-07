# shopping_list_manager.py

def display_menu():
    """Displays the main menu options to the user."""
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """
    Main function to run the shopping list manager.
    It initializes an empty shopping list and handles user interactions.
    """
    shopping_list = [] # Initialize an empty list for the shopping list

    while True: # Loop continuously to display the menu
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Add Item functionality
            item = input("Enter the item to add: ").strip()
            if item: # Ensure item is not empty
                shopping_list.append(item)
                print(f"'{item}' added to the list.")
            else:
                print("Item name cannot be empty.")
        elif choice == '2':
            # Remove Item functionality
            if not shopping_list: # Check if the list is empty first
                print("The shopping list is empty. Nothing to remove.")
                continue # Go back to the menu
            
            item_to_remove = input("Enter the item to remove: ").strip()
            if item_to_remove: # Ensure item name is not empty
                if item_to_remove in shopping_list:
                    shopping_list.remove(item_to_remove)
                    print(f"'{item_to_remove}' removed from the list.")
                else:
                    print(f"'{item_to_remove}' not found in the list.")
            else:
                print("Item name cannot be empty.")
        elif choice == '3':
            # View List functionality
            if not shopping_list: # Check if the list is empty
                print("The shopping list is empty.")
            else:
                print("\n--- Your Shopping List ---")
                for index, item in enumerate(shopping_list, 1): # Enumerate to show numbered list
                    print(f"{index}. {item}")
                print("--------------------------")
        elif choice == '4':
            # Exit functionality
            print("Goodbye!")
            break # Exit the while loop, ending the program
        else:
            # Handle invalid menu choices
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()