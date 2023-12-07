def add_two_to_input():
    try:
        user_input = input("Введите число: ")
        result = 2 + int(user_input)
        print("Результат сложения:", result)
    except ValueError:
        print("Неподходящий тип данных. Ожидалось целое число.")
add_two_to_input()
add_two_to_input()
add_two_to_input()

