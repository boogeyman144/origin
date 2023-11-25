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