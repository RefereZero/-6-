
text = input("Введите текст на русском языке: ")

count = 0
for word in text.split():
    clean_word = word.strip('.,!?;:"()[]{}«»')
    if clean_word and clean_word[0].lower() == 'е':
        count += 1

print(f"Количество слов, начинающихся с буквы 'е': {count}")
