for i in range(10):
    print('i= ', i)
    if i == 0:
        i += 2
    if i == 1 or i == 4:
        continue
    if i == 2 or i == 3:
        print('переменная равна 2 или 3')
    elif i in [5, 6, 7, 8]:
        print('переменная равна 5, 6 или 7, 8')
    else:
        break