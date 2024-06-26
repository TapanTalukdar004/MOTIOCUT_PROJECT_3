from datetime import datetime

# In-memory list to store expenses
expenses = []

# Add a new expense
def add_expense(amount, description, category):
    expense = {
        'amount': amount,
        'description': description,
        'category': category,
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    expenses.append(expense)

# View all expenses
def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return
    for expense in expenses:
        print(f"Amount: {expense['amount']}, Description: {expense['description']}, Category: {expense['category']}, Date: {expense['date']}")

# View expenses by category
def view_expenses_by_category(category):
    filtered_expenses = [e for e in expenses if e['category'].lower() == category.lower()]
    if not filtered_expenses:
        print(f"No expenses found in the category: {category}")
        return
    for expense in filtered_expenses:
        print(f"Amount: {expense['amount']}, Description: {expense['description']}, Category: {expense['category']}, Date: {expense['date']}")

# View monthly summary
def view_monthly_summary(month):
    monthly_expenses = [e for e in expenses if datetime.strptime(e['date'], '%Y-%m-%d %H:%M:%S').strftime('%Y-%m') == month]
    if not monthly_expenses:
        print(f"No expenses found for the month: {month}")
        return
    total = sum(e['amount'] for e in monthly_expenses)
    print(f"Total expenses for {month}: {total}")
    for expense in monthly_expenses:
        print(f"Amount: {expense['amount']}, Description: {expense['description']}, Category: {expense['category']}, Date: {expense['date']}")

# Command-line interface
def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Expenses by Category")
        print("4. View Monthly Summary")
        print("5. Exit")

        choice = input("Choose an option: ")
        
        if choice == '1':
            try:
                amount = float(input("Enter amount: "))
                description = input("Enter description: ")
                category = input("Enter category: ")
                add_expense(amount, description, category)
                print("Expense added successfully.")
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
        
        elif choice == '2':
            view_expenses()
        
        elif choice == '3':
            category = input("Enter category: ")
            view_expenses_by_category(category)
        
        elif choice == '4':
            month = input("Enter month (YYYY-MM): ")
            view_monthly_summary(month)
        
        elif choice == '5':
            print("Exiting Expense Tracker. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
