from math import sqrt
def square():
    a = float(input('введите значение стороны a:'))
    b = float(input('введите значение стороны b:'))
    c = float(input('введите значение стороны c:'))
    p= (a + b + c) / 2
    S= p * (p - a) * (p - b) * (p - c)
    if S <= 0:
        print('треугольника с такими сторонами не существует')
    else:
        square_of_triangle= sqrt(S)
        print(f"Площадь треугольника равна {square_of_triangle}")
