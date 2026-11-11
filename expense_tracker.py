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

def view_expenses(expenses):
    if not expenses:
        print("No expenses yet.")
        return
    for i, e in enumerate(expenses, 1):
        print(f"{i}. {e['category']} - {e['amount']}")

def category_total(expenses):
    if not expenses:
        print("No expenses yet.")
        return
    totals = {}
    for e in expenses:
        totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]
    for cat, total in totals.items():
        print(f"{cat}: {total}")

def main():
    expenses = load_expenses()

    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Category Total")
        print("4. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            category_total(expenses)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
