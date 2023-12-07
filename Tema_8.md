# Тема 8. Введение в ООП
Отчет по Теме #8 выполнил:
- Тептин Владислав Александрович
- АИС-21-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |



## Самостоятельная работа №1
### Самостоятельно создайте класс и его объект
```python
class Car:
    def __init__(self, brand, model, year, fuel_level):
        self.brand = brand
        self.model = model
        self.year = year
        self.fuel_level = fuel_level
        self.engine_started = False
    def start_engine(self):
        if self.fuel_level > 0:
            self.engine_started = True
            print(f"Двигатель {self.brand} {self.model} запущен.")
        else:
            print("Бензобак пуст. Невозможно запустить двигатель.")
    def stop_engine(self):
        self.engine_started = False
        print(f"Двигатель {self.brand} {self.model} остановлен.")
    def refuel(self, fuel_amount):
        self.fuel_level += fuel_amount
        print(f"Долито {fuel_amount} литров бензина. Уровень бензина: {self.fuel_level}")
    def check_status(self):
        print(f"Бренд: {self.brand}")
        print(f"Модель: {self.model}")
        print(f"Год: {self.year}")
        print(f"Уровень топлива: {self.fuel_level}")
        print(f"Статус двигателя: {'On' if self.engine_started else 'Off'}")
```
```python
from Tema8 import Car
my_car = Car("Toyota", "Corolla", 2020, 20) # Объект класса
# Взаимодействие с объектом
my_car.check_status()
my_car.start_engine()
my_car.check_status()
my_car.refuel(15)
my_car.stop_engine()
my_car.check_status()
```
### Результат.
![Меню](https://github.com/boogeyman144/origin/blob/Тема_8/Pic/Tema8_1.png)
![Меню](https://github.com/boogeyman144/origin/blob/Тема_8/Pic/Tema8_1(2).png)

## Вывод
Я попрактиковался в создание классов в python
  
## Самостоятельная работа №2
### Самостоятельно создайте атрибуты и методы для ранее созданного класса

```python
class Car:
    def __init__(self, brand, model, year, fuel_level):
        self.brand = brand
        self.model = model
        self.year = year
        self.fuel_level = fuel_level
        self.engine_started = False
        self.mileage = 0
    def start_engine(self):
        if self.fuel_level > 0:
            self.engine_started = True
            print(f"Двигатель {self.brand} {self.model} запущен.")
        else:
            print("Бензобак пуст. Невозможно запустить двигатель.")
    def stop_engine(self):
        self.engine_started = False
        print(f"Двигатель {self.brand} {self.model} остановлен.")
    def refuel(self, fuel_amount):
        self.fuel_level += fuel_amount
        print(f"Долито {fuel_amount} литров бензина. Уровень бензина: {self.fuel_level}")
    def check_status(self):
        print(f"Бренд: {self.brand}")
        print(f"Модель: {self.model}")
        print(f"Год: {self.year}")
        print(f"Уровень топлива: {self.fuel_level}")
        print(f"Пробег: {self.mileage} км")
        print(f"Статус двигателя: {'On' if self.engine_started else 'Off'}")

    def drive(self, distance):
        if self.engine_started:
            fuel_needed = distance * 0.1
            if self.fuel_level >= fuel_needed:
                self.fuel_level -= fuel_needed
                self.mileage += distance
                print(f"{self.brand} {self.model} проехала {distance} км.")
            else:
                print("Недостаточно топлива, чтобы преодолеть это расстояние.")
        else:
            print("Запустите двигатель, чтобы ехать.")
```
```python
from Tema8 import Car
my_car = Car("Toyota", "Corolla", 2020, 20)
my_car.check_status()
my_car.start_engine()
my_car.drive(50)
my_car.check_status()
my_car.refuel(10)
my_car.drive(30)
my_car.stop_engine()
my_car.check_status()
```
### Результат.
![Меню](https://github.com/boogeyman144/origin/blob/Тема_8/Pic/Tema8_2.png)
![Меню](https://github.com/boogeyman144/origin/blob/Тема_8/Pic/Tema8_2(2).png)

## Самостоятельная работа №3
### Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом.

```python
class Car:
    def __init__(self, brand, model, year, fuel_level):
        self.brand = brand
        self.model = model
        self.year = year
        self.fuel_level = fuel_level
        self.engine_started = False
        self.mileage = 0
    def start_engine(self):
        if self.fuel_level > 0:
            self.engine_started = True
            print(f"Двигатель {self.brand} {self.model} запущен.")
        else:
            print("Бензобак пуст. Невозможно запустить двигатель.")
    def stop_engine(self):
        self.engine_started = False
        print(f"Двигатель {self.brand} {self.model} остановлен.")
    def refuel(self, fuel_amount):
        self.fuel_level += fuel_amount
        print(f"Долито {fuel_amount} литров бензина. Уровень бензина: {self.fuel_level}")
    def check_status(self):
        print(f"Бренд: {self.brand}")
        print(f"Модель: {self.model}")
        print(f"Год: {self.year}")
        print(f"Уровень топлива: {self.fuel_level}")
        print(f"Пробег: {self.mileage} км")
        print(f"Статус двигателя: {'On' if self.engine_started else 'Off'}")

    def drive(self, distance):
        if self.engine_started:
            fuel_needed = distance * 0.1
            if self.fuel_level >= fuel_needed:
                self.fuel_level -= fuel_needed
                self.mileage += distance
                print(f"{self.brand} {self.model} проехала {distance} км.")
            else:
                print("Недостаточно топлива, чтобы преодолеть это расстояние.")
        else:
            print("Запустите двигатель, чтобы ехать.")

class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_level):
        super().__init__(brand, model, year, 0)
        self.battery_level = battery_level
    def charge_battery(self, charge_amount):
        self.battery_level += charge_amount
        print(f"Добавлено {charge_amount}мА зарядки. Заряд батареи: {self.battery_level}")
    def drive(self, distance):
        if self.engine_started:
            if self.battery_level >= distance:
                self.battery_level -= distance
                self.mileage += distance
                print(f"{self.brand} {self.model} проехала {distance} км.")
            else:
                print("Недостаточно зарядки, чтобы преодолеть это расстояние")
        else:
            print("Запустите двигатель, чтобы ехать.")

```
```python
from Tema8 import ElectricCar
my_electric_car = ElectricCar("Tesla", "Model S", 2022, 100)
my_electric_car.check_status()
my_electric_car.start_engine()
my_electric_car.drive(80)
my_electric_car.check_status()
my_electric_car.charge_battery(50)
my_electric_car.drive(120)
my_electric_car.stop_engine()
my_electric_car.check_status()
```
### Результат.
![Меню](https://github.com/boogeyman144/origin/blob/Тема_8/Pic/Tema8_3.png)
![Меню](https://github.com/boogeyman144/origin/blob/Тема_8/Pic/Tema8_3(2).png)

## Вывод
Я попрактиковался в реализации наследования, а также уже на этом этапе реализовал полиморфизм, так как метод drive присутствует в обоих классах под одним названием, но при этом для обычных машин введет расчеты с топливом, а для электромобилей введёт работу с зарядом батареи

## Самостоятельная работа №4
### Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом

```python
class Car:
    def __init__(self, brand, model, year, fuel_level):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__fuel_level = fuel_level
        self.__engine_started = False
        self.__mileage = 0
    def get_brand(self):
        return self.__brand
    def get_model(self):
        return self.__model
    def get_year(self):
        return self.__year
    def get_fuel_level(self):
        return self.__fuel_level
    def get_mileage(self):
        return self.__mileage
    def start_engine(self):
        if self.__fuel_level > 0:
            self.__engine_started = True
            print(f"Двигатель {self.__brand} {self.__model} запущен.")
        else:
            print("Бензобак пуст. невозможно запустить двигатель.")
    def stop_engine(self):
        self.__engine_started = False
        print(f"Двигатель {self.__brand} {self.__model} остановлен.")
    def drive(self, distance):
        if self.__engine_started:
            fuel_needed = distance * 0.1
            if self.__fuel_level >= fuel_needed:
                self.__fuel_level -= fuel_needed
                self.__mileage += distance
                print(f"{self.__brand} {self.__model} проехала {distance} км.")
            else:
                print("Недостаточно топлива, чтобы преодолеть это расстояние.")
        else:
            print("Запустите двигатель, чтобы ехать.")
class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_level):
        super().__init__(brand, model, year, 0)
        self.__battery_level = battery_level
    def get_battery_level(self):
        return self.__battery_level
    def charge_battery(self, charge_amount):
        self.__battery_level += charge_amount
        print(f"Добавлено {charge_amount}мА зарядки. Заряд батареи: {self.__battery_level}")
    def drive(self, distance):
        if self._Car__engine_started:
            if self.__battery_level >= distance:
                self.__battery_level -= distance
                self._Car__mileage += distance
                print(f"{self._Car__brand} {self._Car__model} проехала {distance} км.")
            else:
                print("Недостаточно зарядки, чтобы преодолеть это расстояние.")
        else:
            print("Запустите двигатель, чтобы ехать.")
```
```python
from Tema8 import Car
from Tema8 import ElectricCar
my_car = Car("Toyota", "Corolla", 2020, 20)
print(my_car.get_brand())
print(my_car.get_fuel_level())
my_car.start_engine()
my_car.drive(50)
print(my_car.get_fuel_level())
print(my_car.get_mileage())
my_car.stop_engine()
my_electric_car = ElectricCar("Tesla", "Model S", 2022, 100)
print(my_electric_car.get_brand())
print(my_electric_car.get_battery_level())
my_electric_car.start_engine()
my_electric_car.drive(80)
print(my_electric_car.get_battery_level())
print(my_electric_car.get_mileage())
my_electric_car.stop_engine()
```
### Результат.
![Меню](https://github.com/boogeyman144/origin/blob/Тема_8/Pic/Tema8_4.png)
![Меню](https://github.com/boogeyman144/origin/blob/Тема_8/Pic/Tema8_4(2).png)
