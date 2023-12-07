# Декоратор, который печатает сообщение
def print_message_decorator(func):
    def wrapper(*args, **kwargs):
        print("Декоратор печатает это сообщение")
        return func(*args, **kwargs)
    return wrapper

# Функции, которые используют данный декоратор
@print_message_decorator
def say_hello():
    print("Hello, world!")

@print_message_decorator
def multiply(a, b):
    return a * b

if __name__ == "__main__":
    say_hello()  # Вызываем функцию say_hello
    result = multiply(5, 7)  # Вызываем функцию multiply
    print("Результат умножения:", result)
