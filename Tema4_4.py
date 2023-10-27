def average_values(*args):
    average = sum(args) / len(args)
    print(f"Аргументы: {args}")
    print(f"Среднее арифметическое: {average}")

if __name__ == '__main__':
    average_values(1, 2, 3, 4, 5, 6, 0, 0, 0)

