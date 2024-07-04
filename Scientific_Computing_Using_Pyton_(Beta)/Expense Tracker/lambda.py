def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})

def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))

def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)

def print_expenses(expenses):
    for expense in expenses:
        print(f"amount: {expense['amount']}, category: {expense['category']}")

def main():
    expenses = []
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')

        choice = input('Enter your choice: ')

        if choice == '1':
            print('\n***Add an expense***')
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)
            print('***Expense successfully added!***')
        elif choice == '2':
            print('\n***The list of all expenses***')
            print_expenses(expenses)
        elif choice == '3':
            print('***Total expense is:', total_expenses(expenses),'***')
        elif choice == '4':
            print('\n***Filter expenses by category***')
            category = input('Enter category: ')
            print_expenses(filter_expenses_by_category(expenses, category))
        
        elif choice == '5':
            print('\nHave a nice day!')
            break
        else:
            print('\n***Enter a valid number***')
            continue

main()