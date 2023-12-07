def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            if not content:
                raise Exception("Файл пустой")
            else:
                print("Информация из файла:")
                print(content)
    except FileNotFoundError:
        print("Файл не найден")
    except Exception as e:
        print(e)

# Проверяем пустой файл
print("Чтение файла:")
read_file('test.txt')
