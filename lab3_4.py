numbers = [1, 2, 3, 5, 6, 7, 8, 11, 13, 14, 17, 19, 23]
one = int(input('введите значение переменной: '))
if one in numbers:
    if one % 2 == 0:
        print('переменная четная и есть в данном массиве')
    else:
        print('переменная нечетная и есть в данном массиве')
else:
    print(f"переменной нет в данном массиве и она равна {one}")