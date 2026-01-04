from expense import add_expense
from habit import add_habit
from analysis import analyze_data

while True:
    print("\nSMART EXPENSE & HABIT ANALYZER")
    print("1. Add Expense")
    print("2. Add Habit")
    print("3. View Report")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        add_habit()
    elif choice == "3":
        analyze_data()
    elif choice == "4":
        print("👋 Exiting...")
        break
    else:
        print("❌ Invalid choice")