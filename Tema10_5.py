# Создаем собственное исключение
class InvalidInputError(Exception):
    pass

# Пример использования исключения в первом фрагменте кода
def process_user_input(value):
    try:
        if not isinstance(value, int):
            raise InvalidInputError("Ожидалось целое число")
        result = value * 2
        print(f"Результат удвоения введенного числа: {result}")
    except InvalidInputError as e:
        print(f"Ошибка: {e}")

# Пример использования исключения во втором фрагменте кода
def calculate_square_root(number):
    try:
        if number < 0:
            raise InvalidInputError("Нельзя извлечь корень из отрицательного числа")
        result = number ** 0.5
        print(f"Квадратный корень из числа {number}: {result}")
    except InvalidInputError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    # Первый фрагмент кода
    process_user_input(10)  # Правильный ввод
    process_user_input("abc")  # Некорректный ввод, вызов исключения

    print("\n===========================================\n")

    # Второй фрагмент кода
    calculate_square_root(25)  # Правильный ввод
    calculate_square_root(-9)  # Некорректный ввод, вызов исключения
