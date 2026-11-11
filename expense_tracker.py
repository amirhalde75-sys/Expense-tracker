
import json

FILE_NAME = "expenses.json"

def load_expenses():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return []

def save_expenses(expenses):
    with open(FILE_NAME, "w") as f:
        json.dump(expenses, f, indent=4)

def add_expense(expenses):
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Number daalo.")
        return
    if amount <= 0:
        print("Amount 0 se zyada hona chahiye.")
        return
    category = input("Enter category (Food/Travel): ").strip().title()
    if not category:
        print("Category khaali nahi ho sakti.")
        return
    expenses.append({"amount": amount, "category": category})
    save_expenses(expenses)
    print("Expense added and saved!")
