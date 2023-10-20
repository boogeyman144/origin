string = input('введите строку: ')
letter = input('введите букву для поиска: ')
for i in string:
    if i == letter:
        index = string.find(letter)
        print(f"буква '{letter}' есть в строке под {index} индексом")
        break
else:
    print(f"буквы '{letter}' нет в строке")