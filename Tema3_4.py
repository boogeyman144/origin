line = input('введите предложение на английском: ').lower()
sum = 0
for letter in line:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        sum += 1
sentence = line.replace('ugly', 'beauty')
print(f"длина предложения {len(line)} символов. \nпредложение в нижнем регистре: {line} \nколичество гласных равно {sum}."
      f"\nпредложение с заменнёными словами: {sentence} \nначинается ли предложение на 'the': {line.startswith('the')}"
      f"\nзаканчивается ли предложение на 'end': {line.endswith('end')}")