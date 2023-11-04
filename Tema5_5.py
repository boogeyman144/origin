def transform_and_repeat(number, count):
    transformed_values = set()
    str_number = str(number)
    for i in range(1, count + 1):
        transformed_values.add(str_number * i)
    transformed_values.add(number)
    return transformed_values
def process_list(input_list):
    result_set = set()
    count_dict = {}
    for num in input_list:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    for num, count in count_dict.items():
        transformed_values = transform_and_repeat(num, count)
        result_set.update(transformed_values)
    return result_set
list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]
result_set_1 = process_list(list_1)
result_set_2 = process_list(list_2)
result_set_3 = process_list(list_3)
print(result_set_1)
print(result_set_2)
print(result_set_3)