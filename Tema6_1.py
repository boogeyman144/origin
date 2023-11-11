Number = input("Введите последовательность чисел, разделенных пробелом: ").split()
number_list = [int(num) for num in Number]
number_tuple = tuple(number_list)
print("Список:", number_list)
print("Кортеж:", number_tuple)