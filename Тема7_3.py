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
