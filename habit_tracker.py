# Habit Tracker
# Created by Lauren Copas
# May 2025

import json  # to work with JSON files
import os  # to check if a file exists


# Create a function which will read from habits.json and returns the habits data
def load_habits():
    if not os.path.exists("habits.json"):  # checks whether the file exists
        return []  # if the file doesn't exist, will return an empty list (no habits yet)
    with open("habits.json", "r") as file:  # opens the file in read mode
        try:  # to try to load the file safely
            return json.load(file)
        except json.JSONDecodeError:  # catches the error if the file is empty or corrupted
            return []  # fallback - return an empty list again


# Create a function which will take current list of habits and write to file
def save_habits(habits):
    with open("habits.json", "w") as file:  # opens the file in write mode (overwrite it)
        json.dump(habits, file, indent=4)  # writes the list of habits into the file using neat formatting


# Create a function which will ask the user for a habit name, check if the habit already exists and if it doesn't, it
# will add it to the list and return it
def add_new_habit(habits):  # take the current list as input
    new_habit = input("Well done on starting a new habit! Enter the name of the habit you'd like to track:").strip()
    # strip to remove leading/trailing spaces

    # loop through each existing habit and compare them to the new one, all in lowercase.
    # If it already exists, tell user and don't add it again
    for habit in habits:
        if habit["habit"].lower() == new_habit.lower():
            print("That habit already exists!")
            return habits  # return the list unchanged

    habits.append({  # add a new dictionary to the list
        "habit": new_habit,  # the name of the new habit
        "dates": []  # currently an empty list, to be filled in later
    })
    print(f"Success! Habit '{new_habit}' has been added!\n")
    return habits


# welcome screen and menu
def main():
    habits = load_habits()

    while True:
        print("\n*** Welcome to Happy Habits Tracker! ***")
        print("Please choose from one of the following options:")
        print("1. View habits")
        print("2. Add a new habit")
        print("3. Mark habit as done today")
        print("4. Exit")
        choice = input("Enter the number that corresponds to your choice:")

        if choice == '1':
            print("*** You chose to view habits. ***")
        elif choice == '2':
            habits = add_new_habit(habits)  # updating habits list with new one returned from add_new_habit()
            save_habits(habits)  # save new habit to habits.json
        elif choice == '3':
            print("*** You chose to mark a habit as done today ***")
        elif choice == '4':
            print("*** Goodbye, and happy habit tracking! ***")
            break
        else:
            print("*** Whoops! That wasn't a valid option. Please enter either 1, 2, 3 or 4. ***")


if __name__ == "__main__":
    main()



