# Habit Tracker
# Created by Lauren Copas
# May 2025

import json  # to work with JSON files
import os  # to check if a file exists
from datetime import date, timedelta, datetime  # allows me to access the current date needed to mark habits as done
# timedelta will allow me to check if two dates are no more than 1 day apart, to create a 'streak' for the user


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


# Create a function that will print the different habits as well as the number of days each habit has been logged
def view_habits(habits):
    if not habits:  # this will check if the habits list is still empty, and if so, it will display a message
        # and then stop
        print("Looks like you haven't added any habits yet!")
        return

    print("\nYour Habits:")
    for habit in habits:
        name = habit["habit"]  # fetch the habit
        count = len(habit["dates"])  # count the number of times the particular habit has been logged for
        streak = get_streak(habit["dates"])
        print(f" {name}: {count} days logged. \n🔥🔥🔥 You're on fire - {streak} days so far. Keep going!")


# Create a function that will allow the user to mark their habit as done on that particular day. It will also offer
# the user some words of encouragement!
def mark_habit_done(habits):
    if not habits:  # if no habits have been created yet, we can return it without making any changes
        print("You need to add a habit before you can mark it as done!")
        return habits

    print("\nWhich habit do you want to mark as completed today?")
    for index, habit in enumerate(habits, start=1):  # use enumerate to ensure the numbers start from 1, instead of 0
        print(f"{index}.{habit['habit']}")

    try:
        choice = int(input("Enter the number of the habit you completed:"))
        selected_habit = habits[choice - 1]  # 1 has to be subtracted because indexes begin at 0
        today = str(date.today())  # convert to a string so that it matches the format in the dates list

        if today in selected_habit["dates"]:
            print("Looks like you've already marked this habit as done today")  # to ensure current day not duplicated
        else:
            selected_habit["dates"].append(today)
            print(f"Awesome work! '{selected_habit['habit']}' is marked as done for today.")  # print a message to
        # acknowledge that habit is logged for the day, and also give the user some positive reinforcement!
    except (ValueError, IndexError):
        print("That hasn't worked. Please make sure to enter a number from the list.")

    return habits


# Create a function that will show how many consecutive days a user has logged a particular habit - called a streak.
def get_streak(dates_list):
    if not dates_list:
        return 0

    # I want to convert the date strings to date objects to sort them
    # first, I need to convert the date string into a real date object using datetime.strptime
    # then, I want to sort the dates so that they can be checked in order (using sorted)
    date_objects = sorted([datetime.strptime(d, "%Y-%m-%d").date() for d in dates_list])

    streak = 1
    max_streak = 1

    # I want it to compare each date to the date before, and if it's exactly 1 day apart, continue the streak
    for i in range(1, len(date_objects)):
        if date_objects[i] - date_objects[i -1] == timedelta(days=1):
            streak += 1
            max_streak = max(max_streak, streak)
        else:
            # if it isn't exactly 1 day apart, I want the streak to reset to 1
            streak = 1

    return max_streak


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
            view_habits(habits)
        elif choice == '2':
            habits = add_new_habit(habits)  # updating habits list with new one returned from add_new_habit()
            save_habits(habits)  # save new habit to habits.json
        elif choice == '3':
            habits = mark_habit_done(habits)
            save_habits(habits)
        elif choice == '4':
            print("*** Goodbye, and happy habit tracking! ***")
            break
        else:
            print("*** Whoops! That wasn't a valid option. Please enter either 1, 2, 3 or 4. ***")


if __name__ == "__main__":
    main()
