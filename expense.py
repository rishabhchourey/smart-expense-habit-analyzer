import json
from datetime import datetime

FILE_PATH = "data/expenses.json"

def load_expenses():
    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except:
        return []

def save_expense(expense):
    expenses = load_expenses()
    expenses.append(expense)
    with open(FILE_PATH, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter category (Food/Travel/Study/Other): ")
    amount = float(input("Enter amount: "))

    expense = {
        "date": date,
        "category": category,
        "amount": amount
    }

    save_expense(expense)
    print("✅ Expense added successfully!")