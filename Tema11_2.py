def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Запись чисел Фибоначчи в файл
n = 200
with open("fib.txt", "w") as file:
    fibonacci_sequence = fib(n)
    for num in fibonacci_sequence:
        file.write(str(num) + "\n")
