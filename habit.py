import json
from datetime import datetime

FILE_PATH = "data/habits.json"

def load_habits():
    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except:
        return []

def save_habit(habit):
    habits = load_habits()
    habits.append(habit)
    with open(FILE_PATH, "w") as file:
        json.dump(habits, file, indent=4)

def add_habit():
    date = datetime.now().strftime("%Y-%m-%d")
    habit_name = input("Enter habit name: ")
    status = input("Completed? (yes/no): ")

    habit = {
        "date": date,
        "habit": habit_name,
        "status": status.lower()
    }

    save_habit(habit)
    print("✅ Habit recorded successfully!")