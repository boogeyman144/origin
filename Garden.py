class Tomato:
    states = ('отсутствует', 'цветение', 'зеленый', 'красный')

    def __init__(self, index):
        self._index = index  # свойство _index используется для хранения индекса помидора
        self._state = 0  # свойство _state используется для хранения стадии созревания помидора
        # оба свойства являются защищёными атрибутами
    def grow(self):
        # Метод, переводящий томат на следующую стадию созревания.
        # Если томат уже находится на последней стадии созревания, метод не делает ничего.
        if self._state < len(self.states) - 1:
            self._state += 1
            print(f"Томат {_index} перешел на стадию {self.states[self._state]}")

    def is_ripe(self):
        #  Метод, проверяющий, что томат полностью созрел.
        #  Возвращает True, если томат находится на последней стадии созревания, иначе False.
        ripeness = self.states[self._state]
        if self._state == len(self.states) - 1:
            print(f"Томат {_index} полностью созрел (стадия {ripeness})")
            return True
        else:
            print(f"Томат {_index} еще не полностью созрел (стадия {ripeness})")
            return False



class TomatoBush:
    def __init__(self, num_tomatoes):
        # Инициализирует список помидоров заданного количества.
        self.tomatoes = [Tomato(index) for index in range(1, num_tomatoes + 1)]

    def grow_all(self):
        # Метод, переводящий все помидоры на следующую стадию созревания.
        for tomato in self.tomatoes:
            if tomato._state < len(Tomato.states) - 1:
                tomato._state += 1

    def all_are_ripe(self):
        # Метод, проверяющий, все ли помидоры на кусте полностью созрели.
        return all(tomato._state == len(Tomato.states) - 1 for tomato in self.tomatoes)

    def give_away_all(self):
        #  Метод, собирающий урожай (очищает список помидоров после сбора урожая).
        self.tomatoes = [Tomato(index + 1) for index in range(len(self.tomatoes))]


class Gardener:
    def __init__(self, name, plant):
        self.name = name  # публичный атрибут
        self._plant = plant  # защищеный атрибут

    def work(self):
        # с помощбю метода класса TomatoBush добовляет зрелость всем помидорам, а также выводит их статус в консоль
        self._plant.grow_all()
        print("Текущее состояние помидоров после работы садовника:")
        for tomato in self._plant.tomatoes:
            print(f"Помидор {tomato._index}: {Tomato.states[tomato._state]}")

    def harvest(self):
        if self._plant.all_are_ripe():
            print("Урожай созрел! Садовник собирает урожай.")
            self._plant.give_away_all()
        else:
            print("Пока не все плоды созрели, подождите еще немного.")

    @staticmethod
    def knowledge_base():
        print("Справка по садоводству:")
        print("- Создайте куст с помидорами (TomatoBush) и садовника (Gardener).")
        print("- Садовник может ухаживать за растением и собирать урожай.")
        print("- Растение, за которым ухаживает садовник, имеет методы для роста и проверки зрелости помидоров.")
