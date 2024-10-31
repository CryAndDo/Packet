from collections import Counter

def count_russian_and_latin_letters(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    russian_letters = set("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
    latin_letters = set("abcdefghijklmnopqrstuvwxyz")

    counter = Counter(text.lower())

    total_russian = sum(counter[letter] for letter in russian_letters)
    total_latin = sum(counter[letter] for letter in latin_letters)

    if total_russian > total_latin:
        result = "Русских букв больше."
    elif total_russian < total_latin:
        result = "Латинских букв больше."
    else:
        result = "Количество русских и латинских букв одинаково."

    print(result)
    return result

from mypackage.module2 import count_russian_and_latin_letters

file_path = 'text.txt'

count_russian_and_latin_letters(file_path)
