import json

def analyze_data():
    with open("data/expenses.json", "r") as f:
        expenses = json.load(f)

    with open("data/habits.json", "r") as f:
        habits = json.load(f)

    total_expense = sum(e["amount"] for e in expenses)

    category_summary = {}
    for e in expenses:
        category_summary[e["category"]] = category_summary.get(e["category"], 0) + e["amount"]

    completed_habits = sum(1 for h in habits if h["status"] == "yes")
    habit_percentage = (completed_habits / len(habits)) * 100 if habits else 0

    print("\n📊 MONTHLY REPORT")
    print("--------------------")
    print(f"Total Expense: ₹{total_expense}")
    print(f"Highest Expense Category: {max(category_summary, key=category_summary.get)}")
    print(f"Habit Consistency: {habit_percentage:.2f}%")

    if habit_percentage < 70:
        print("⚠️ Improve your habits consistency.")
    if category_summary.get("Food", 0) > total_expense * 0.4:
        print("⚠️ High food expenses detected.")