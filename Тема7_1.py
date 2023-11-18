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
