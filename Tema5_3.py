def triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area
one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]
max_one = max(one)
min_one = min(one)
max_two = max(two)
min_two = min(two)
max_three = max(three)
min_three = min(three)
area_one_max = triangle_area(max_one, max_two, max_three)
area_two_min = triangle_area(min_one, min_two, min_three)

# Вывод результата в консоль
print("Площадь треугольника, составленного из максимальных элементов:", area_one_max)
print("Площадь треугольника, составленного из минимальных элементов:", area_two_min)
