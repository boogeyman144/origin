def extract_employee_data(data_tuple, employee_id):
    if employee_id not in data_tuple:
        return ()
    start_index = data_tuple.index(employee_id)
    end_index = len(data_tuple) - data_tuple[::-1].index(employee_id) - 1
    if start_index == end_index:
        return data_tuple[start_index:]
    return data_tuple[start_index:end_index + 1]
data_tuple1 = (1, 2, 3)
data_tuple2 = (1, 8, 3, 4, 8, 8, 9, 2)
data_tuple3 = (1, 2, 8, 5, 1, 2, 9)
employee_id1 = 8
result1 = extract_employee_data(data_tuple1, employee_id1)
result2 = extract_employee_data(data_tuple2, employee_id1)
result3 = extract_employee_data(data_tuple3, employee_id1)
print(result1)
print(result2)
print(result3)
