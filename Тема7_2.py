def save_expenses(expenses, file_name):
    with open(file_name, 'w') as file:
        for category, amounts in expenses.items():
            file.write(f"{category}:{','.join(map(str, amounts))}\n")
def load_expenses(file_name):
        with open(file_name, 'r') as file:
            return {category: list(map(float, amounts.split(','))) for line in file if (category := line.strip().split(':')[0]) for amounts in [line.strip().split(':')[1]]}
def add_expense(expenses, category, amount):
    expenses.setdefault(category, []).append(amount)
    return expenses
def show_expenses(expenses):
    if not expenses:
        print("Нет информации о расходах.")
        return
    print("Информация о расходах:")
    for category, amounts in expenses.items():
        print(f"{category}: {sum(amounts)}")
def main():
    file_name = 'expenses.txt'
    expenses = load_expenses(file_name)
    while True:
        print("1. Добавить расход")
        print("2. Показать расходы")
        print("3. Выход")
        choice = input("Введите номер действия: ")
        if choice == '1':
            category = input("Введите категорию расхода: ")
            amount = float(input("Введите сумму расхода: "))
            expenses = add_expense(expenses, category, amount)
            save_expenses(expenses, file_name)
            print("Расход успешно добавлен!")
        elif choice == '2':
            show_expenses(expenses)
        elif choice == '3':
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")
if __name__ == "__main__":
    main()