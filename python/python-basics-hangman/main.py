import json

from datetime import datetime
from game import game


def get_history():
    with open('shown_words.json', encoding='utf-8') as file:
        shown_words = json.load(file)['shown_words']
        if shown_words:
            for shown_word in shown_words:
                date = datetime.fromisoformat(shown_word['date'])
                date = date.strftime('%Y/%m/%d %H:%M:%S')
                category = shown_word['category']
                word = shown_word['word']
                print(f'{date} | Категория: {category} | Слово: {word}')
        else:
            print('История пуста')


def menu():
    while True:
        print('\n\n\tHangman!\n\n')
        print('Укажите цифру, чтобы:')
        print('1.Начать')
        print('2.Посмотреть прошлые слова')
        print('3.Выйти')

        option = input()

        if option == '1':
            game()
        elif option == '2':
            get_history()
        elif option == '3':
            break


menu()
