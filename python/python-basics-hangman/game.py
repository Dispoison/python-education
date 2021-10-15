import json
import os
import datetime
from random import randint


def update_shown_words(date, category, word):
    shown_word = {'date': date, 'category': category, 'word': word}
    with open('shown_words.json', 'r+', encoding='utf-8') as file:
        words = json.load(file)
        words['shown_words'].insert(0, shown_word)
        file.seek(0)
        json.dump(words, file, indent=4)


def choose_category():
    with open('words.json') as file:
        words = json.load(file)
    while True:
        print('Выберите категорию слов:')
        for i, category in enumerate(words['categories']):
            print(f'{i + 1}. {words["categories"][i]["name"]}')

        input_data = input()
        try:
            input_as_int = int(input_data)
        except ValueError:
            print('Неверный символ!')
            continue
        if 1 <= input_as_int <= len(words['categories']):
            date = datetime.datetime.now().isoformat()
            words_in_category = words['categories'][input_as_int - 1]['words']
            word = words_in_category[randint(0, len(words_in_category) - 1)]
            category = words['categories'][input_as_int - 1]['name']
            update_shown_words(date, category, word)

            return category, word


def get_stages():
    with open('hangman_stages.txt', encoding='utf-8') as file:
        hangman_stages = file.read().split(',')
    return hangman_stages


def display(stages, stage_number, alphabet, used_chars, guessed_chars, category, word, message):
    os.system('clear')

    attempts = len(stages)-stage_number-1
    if attempts > 4 or attempts == 0:
        attempts_word = "попыток"
    elif attempts > 1:
        attempts_word = "попытки"
    else:
        attempts_word = "попытка"

    print(stages[stage_number], end=f'\t{attempts} {attempts_word}\n')
    print(f'Категория: {category}')

    for char in word:
        if char in guessed_chars:
            print(char, end='')
        else:
            print('_', end='')

    print(f'\nОставшиеся: |', end='')
    for char in sorted(list(alphabet)):
        if char in used_chars:
            print(' ', end=' ')
        else:
            print(char, end=' ')
    print('|')

    if message:
        print(message.pop())


def game():
    category, word = choose_category()
    alphabet = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    word_chars = set(word)
    used_chars = set()
    guessed_chars = set()
    message = []

    stages = get_stages()
    stage_number = 0
    while stage_number < len(stages):
        display(stages, stage_number, alphabet, used_chars, guessed_chars, category, word, message)

        if stage_number == len(stages)-1:
            print('Ты проиграл... его вздёрнули')
            break

        if len(guessed_chars) == len(word_chars):
            print('Ты выиграл!')
            break

        input_char = input()
        if input_char not in alphabet:
            message.append('Неверный символ!')
            continue
        elif input_char in used_chars:
            message.append('Эта буква уже была введена!')
            continue
        elif input_char in word_chars - guessed_chars:
            guessed_chars.add(input_char)
            used_chars.add(input_char)
            continue
        elif input_char in alphabet - used_chars:
            used_chars.add(input_char)
            message.append('Неправильная буква :(')

        stage_number += 1
