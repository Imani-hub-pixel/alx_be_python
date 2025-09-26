def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            item=input("Enter the item to enter:")
            shopping_list.append(item)
            print(f"{item} added to the list")
            
        elif choice == 2:
            if len(shopping_list)==0:
                print("The list is empty, nothing to remove")
            else:
                item=input("Enter the item to remove:")
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"{item} removed from the list")
                else:
                    print(f"{item} not found in the list")
        elif choice == 3:
            if len(shopping_list)==0:
                print("The list is empty")
            else:
                print("SHOPPING LIST:")
                for i, item in enumerate(shopping_list):
                    print(f"{i+1}. {item}")
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    