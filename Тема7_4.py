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
