import random

def roll_dice():
    dice = random.randint(1, 6)
    print(f"Кубик: {dice}")

    if dice in [5, 6]:
        print("Вы победили")
    elif dice in [3, 4]:
        print("Перебрасываем кубик")
        roll_dice()
    else:
        print("Вы проиграли")

if __name__ == '__main__':
    roll_dice()