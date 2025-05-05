# Habit Tracker
# Created by Lauren Copas
# May 2025

# welcome screen and menu
def main():
    while True:
        print("\n******* Welcome to Happy Habits Tracker! *******")
        print("Please choose from one of the following options:")
        print("1. View habits")
        print("2. Add a new habit")
        print("3. Mark habit as done today")
        print("4. Exit")

        choice = input("Enter the number that corresponds to your choice:")

        if choice == '1':
            print("You chose to view habits.")
        elif choice == '2':
            print("You chose to add a new habit.")
        elif choice == '3':
            print("You chose to mark a habit as done today")
        elif choice == '4':
            print("Goodbye, and happy habit tracking!")
            break
        else:
            print("Whoops! That wasn't a valid option. Please enter either 1, 2, 3 or 4.")
