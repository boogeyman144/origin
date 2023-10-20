value = 0
while value < 100:
    if value == 0:
        value += 10
    elif value // 5 > 1:
        value *= 3
    else:
        value -= 1
    print(value)
