# Expense Tracker

A simple Python command-line program to track expenses.

## Features
- Add an expense with an amount and a category (e.g. Food, Travel)
- View all expenses
- See the total for each category
- Data is saved in `expenses.json`, so it is loaded again after restarting
- Wrong input (like "abc" as amount) does not crash the program

## How to run
1. Install Python 3
2. Run: `python expense_tracker.py`
3. Choose an option from the menu (1 to 4)

## Functions
- `load_expenses()`: reads expenses from expenses.json
- `save_expenses()`: writes expenses to expenses.json
- `add_expense()`: asks amount and category, adds and saves it
- `view_expenses()`: prints all expenses
- `category_total()`: prints total for each category
