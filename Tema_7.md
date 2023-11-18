# Тема 7. Работа с файлами (ввод, вывод)
Отчет по Теме #7 выполнил:
- Тептин Владислав Александрович
- АИС-21-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |
| Задание 6 | + |  
| Задание 7 | + |  
| Задание 8 | + |  
| Задание 9 | + |  
| Задание 10 | + |  


## Самостоятельная работа №1
### Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит самое часто встречающееся слово.

```python
from collections import Counter
import string
def count_words_and_most_common(file_name):
        with open(file_name, 'r', encoding='utf-8') as file:
            text = file.read()
            words = text.split()
            word_count = len(words)
            word_freq = Counter(words)
            most_common_word = word_freq.most_common(1)
            print(f"Количество слов: {word_count}")
            print(f"Самое часто встречающееся слово: {most_common_word[0][0]}")
count_words_and_most_common('Tema7_1.txt')
```
### Результат.
![Меню](https://github.com/boogeyman144/origin/blob/Тема_7/Pic/Тема7_1.png)
![Меню](https://github.com/boogeyman144/origin/blob/Тема_7/Pic/Тема7_1(2).png)

## Вывод
Я попрактиковался в подсчёте количества слов в файле
  
## Самостоятельная работа №2
### У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль.

```python
def save_expenses(expenses, file_name):
    with open(file_name, 'w') as file:
        for category, amounts in expenses.items():
            file.write(f"{category}:{','.join(map(str, amounts))}\n")
def load_expenses(file_name):
        with open(file_name, 'r') as file:
            return {category: list(map(float, amounts.split(','))) for line in file if (category := line.strip().split(':')[0]) for amounts in [line.strip().split(':')[1]]}
def add_expense(expenses, category, amount):
    expenses.setdefault(category, []).append(amount)
    return expenses
def show_expenses(expenses):
    if not expenses:
        print("Нет информации о расходах.")
        return
    print("Информация о расходах:")
    for category, amounts in expenses.items():
        print(f"{category}: {sum(amounts)}")
def main():
    file_name = 'expenses.txt'
    expenses = load_expenses(file_name)
    while True:
        print("1. Добавить расход")
        print("2. Показать расходы")
        print("3. Выход")
        choice = input("Введите номер действия: ")
        if choice == '1':
            category = input("Введите категорию расхода: ")
            amount = float(input("Введите сумму расхода: "))
            expenses = add_expense(expenses, category, amount)
            save_expenses(expenses, file_name)
            print("Расход успешно добавлен!")
        elif choice == '2':
            show_expenses(expenses)
        elif choice == '3':
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")
if __name__ == "__main__":
    main()
```
### Результат.
![Меню](https://github.com/boogeyman144/origin/blob/Тема_7/Pic/Тема7_2.png)
![Меню](https://github.com/boogeyman144/origin/blob/Тема_7/Pic/Тема7_2(2).png)

## Вывод
  Я попрактиковался в записи данных в файл, а также выводе этих данных в консоль
  
## Самостоятельная работа №3
Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк. 

```python
def count_stats(file_name):
        with open(file_name, 'r', encoding='utf-8') as file:
            text = file.read()
            latin_letters = sum(1 for char in text if char.isalpha() and char.isascii())
            words = text.split()
            num_words = len(words)
            lines = text.splitlines()
            num_lines = len(lines)
            print(f"Количество букв латинского алфавита: {latin_letters}")
            print(f"Число слов: {num_words}")
            print(f"Число строк: {num_lines}")
count_stats('input.txt')
```
### Результат.
![Меню](https://github.com/boogeyman144/origin/blob/Тема_7/Pic/Тема7_3.png)

## Самостоятельная работа №4
### Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра.

```python
import re
def censor_sentence(sentence, banned_words):
    words = re.findall(r"[\w']+|[.,!?; ]", sentence)
    for i in range(len(words)):
        word = words[i]
        if word.lower().strip(".,!?; ") in banned_words:
            words[i] = '*' * len(word)
    censored_sentence = ''.join(words)
    return censored_sentence
def load_banned_words(file_name):
        with open(file_name, 'r', encoding='utf-8') as file:
            banned_words = file.read().split()
            return [word.lower() for word in banned_words]
def main():
    banned_words = load_banned_words('input2.txt')
    if not banned_words:
        print("Запрещенные слова не загружены. Программа завершает работу.")
        return
    sentence = input("Введите предложение: ")
    censored_sentence = censor_sentence(sentence, banned_words)
    print("Предложение с замененными запрещенными словами:")
    print(censored_sentence)
if __name__ == "__main__":
    main()
```
### Результат.
![Меню](https://github.com/boogeyman144/origin/blob/Тема_7/Pic/Тема7_4.png)

## Вывод
Я попрактиковался в замене слов в файле
 
## Самостоятельная работа №5
### Самостоятельно придумайте и решите задачу, которая будет взаимодействовать с текстовым файлом.
Напишите программу, которая будет считать количество имён пользователей и выводить их в алфавитном порядке.

```python
def read_usernames(file_name):
        with open(file_name, 'r', encoding='utf-8') as file:
            usernames = [line.strip() for line in file]
            return usernames
def main():
    file_name = 'users.txt'
    usernames = read_usernames(file_name)
    if not usernames:
        print("Список пользователей не загружен. Программа завершает работу.")
        return
    num_users = len(usernames)
    print(f"Количество пользователей: {num_users}")
    sorted_usernames = sorted(usernames)
    print("Имена пользователей в алфавитном порядке:")
    for username in sorted_usernames:
        print(username)
if __name__ == "__main__":
    main()
```
### Результат.
![Меню](https://github.com/boogeyman144/origin/blob/Тема_7/Pic/Тема7_5.png)
![Меню](https://github.com/boogeyman144/origin/blob/Тема_7/Pic/Тема7_5(2).png)

## Вывод
Я попрактиковался в сортировке данных из файла при выводе их в консоль
