def remove_from_tuple(tup, value):
    try:
        index = tup.index(value)
    except ValueError:
        return tup
    new_tup = tup[:index] + tup[index + 1:]
    return new_tup
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2)
tuple3 = (2, 4, 6, 6, 4, 2)
result1 = remove_from_tuple(tuple1, 1)
result2 = remove_from_tuple(tuple2, 3)
result3 = remove_from_tuple(tuple3, 9)
print(result1)
print(result2)
print(result3)
