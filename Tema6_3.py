def count_of_numbers(input_string):
    if len(input_string) < 15:
        raise ValueError("Длина строки должна быть не менее 15 символов")
    number_count = {}
    for number in input_string:
        number = int(number)
        number_count[number] = number_count.get(number, 0) + 1
    sorted_number_count = sorted(number_count.items(), key=lambda x: x[1], reverse=True)
    top_three_numbers = sorted_number_count[:3]
    result_dict = {number: count for number, count in sorted(top_three_numbers)}
    return result_dict
input_string = "31415926535897932384626433832795"
result = count_of_numbers(input_string)
print(f"Три самых часто встречаемых числа: {result}")

