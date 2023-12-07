def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Пример использования
n = 200
fibonacci_sequence = fib(n)
for num in fibonacci_sequence:
    print(num)
