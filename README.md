# smart-expense-habit-analyzer
Python CLI based expense &amp; habit tracker

## 📌 Project Overview
Smart Expense & Habit Analyzer is a **Python-based CLI application** designed to help users track their daily expenses and habits in a simple and effective way.  
The project focuses on using **core Python concepts** to solve a real-life problem related to money management and personal productivity.

This project stores user data locally and performs **rule-based analysis** to generate meaningful insights and suggestions.

## 🎯 Objective of the Project
- To track daily expenses category-wise  
- To monitor daily habits and their consistency  
- To analyze spending patterns and habit performance  
- To provide smart suggestions using logical conditions  

This project was created to strengthen **Python logic, file handling, and problem-solving skills**.

## ⚙️ Features
- Add daily expenses (Food, Travel, Study, Other)
- Track daily habits (Exercise, Study, etc.)
- Automatic calculation of total expenses
- Category-wise expense analysis
- Habit consistency percentage calculation
- Rule-based smart suggestions
- Simple and user-friendly CLI menu

## 🧰 Technologies & Concepts Used
- Python (Core)
- Functions & Modular Programming
- Lists & Dictionaries
- File Handling
- JSON for data storage
- Datetime module
- Conditional statements & loops


## 🗂 Project Structure
smart_expense_habit_analyzer/
│
├── main.py # Main menu and program flow
├── expense.py # Expense-related functions
├── habit.py # Habit tracking functions
├── analysis.py # Data analysis and report generation
│
├── data/
│ ├── expenses.json
│ ├── habits.json
│
└── README.md

## ▶️ How to Run the Project
1. Clone or download the repository
2. Make sure Python is installed on your system
3. Open terminal or command prompt
4. Navigate to the project folder
5. Run the following command:

```bash
python main.py

## 📊 Sample Output
SMART EXPENSE & HABIT ANALYZER

1. Add Expense
2. Add Habit
3. View Report
4. Exit

Total Expense: ₹6200
Highest Expense Category: Food
Habit Consistency: 68%
⚠️ Improve your habit consistency.
⚠️ High food expenses detected.
