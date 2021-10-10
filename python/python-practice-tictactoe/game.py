from area import Area
from player import Player


class Game:
    def __init__(self, log):
        self.log = log

    @staticmethod
    def _define_round_word(round_num):
        if round_num == 1:
            return 'раунд'
        elif 1 < round_num < 5:
            return 'раунда'
        else:
            return 'раундов'

    @staticmethod
    def _define_draw_word(round_num):
        if round_num == 1:
            return 'ничья'
        elif 1 < round_num < 5:
            return 'ничьи'
        else:
            return 'ничьих'

    @staticmethod
    def _register_players():
        first_player_name = input('Введите имя первого игрока[X] ')
        second_player_name = input('Введите имя второго игрока[O] ')
        first_player = Player(first_player_name, 'X')
        second_player = Player(second_player_name, 'O')
        round_score = [0, 0, 0]
        return first_player, second_player, round_score

    def start(self):
        first_player, second_player, round_score = self._register_players()
        self.log.logger.info(f'*** Игроки {first_player} и {second_player} начали игру ---')
        area = Area(first_player, second_player)
        while True:
            area.display()

            sign, winner = area.is_end_game()
            if winner is not None or sign == 'draw':
                if sign == 'X':
                    round_score[0] += 1
                elif sign == 'O':
                    round_score[1] += 1
                elif sign == 'draw':
                    round_score[2] += 1

                draw = f'и {round_score[2]} {self._define_draw_word(round_score[2])}' if round_score[2] > 0 else ''

                if winner is not None:
                    self.log.logger.info(f'{winner} выиграл! Общий счет: {first_player} '
                                         f'{round_score[0]} / {round_score[1]} {second_player} {draw}')
                elif sign == 'draw':
                    self.log.logger.info(f'Ничья! Общий счет: {first_player} '
                                         f'{round_score[0]} / {round_score[1]} {second_player} {draw}')

                answer = input('Хотите сыграть снова?[y/n] ').lower()
                if answer == 'y':
                    area = Area(first_player, second_player)
                    continue
                else:
                    break

            try:
                area.action_handler()
            except ValueError as e:
                print(f'Ошибка: {e}')
        elapsed_rounds = round_score[0] + round_score[1] + round_score[2]
        round_word = self._define_round_word(elapsed_rounds)
        self.log.logger.info(f'--- Игроки {first_player} и {second_player} завершили игру проведя '
                             f'{elapsed_rounds} {round_word} ***')
