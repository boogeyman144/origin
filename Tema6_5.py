def calculate_average(number_list):
    if not number_list:
        return None
    total = sum(number_list)
    average = total / len(number_list)
    return average
test_list1 = [5, 10, 15, 20, 25]
result1 = calculate_average(test_list1)
print(f"Тест 1: Среднее арифметическое {result1}")
test_list2 = [-2, -4, -6, -8, -10]
result2 = calculate_average(test_list2)
print(f"Тест 2: Среднее арифметическое {result2}")
test_list3 = []
result3 = calculate_average(test_list3)
print(f"Тест 3: Среднее арифметическое {result3}")
