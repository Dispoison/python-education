from game import Game
from log import Log


def print_log(file_name):
    with open(file_name) as file:
        print(file.read())


def main():
    log = Log('game.log')
    game = Game(log)
    while True:
        print('\n\n\tTic-Tac-Toe!\n\n')
        print('Укажите цифру, чтобы:')
        print('1.Начать')
        print('2.Посмотреть лог побед')
        print('3.Очистить лог побед')
        print('4.Выход')

        option = input()

        if option == '1':
            game.start()
        elif option == '2':
            print_log(log.file_name)
        elif option == '3':
            answer = input('Вы уверенны что хотите очистить лог файл?[y/n] ')
            if answer == 'y':
                log.clear_log()
            else:
                print('Отмена очистки лога')
        elif option == '4':
            break


if __name__ == '__main__':
    main()
