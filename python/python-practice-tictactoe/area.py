class Area:
    MAP_MARKS = '123', 'abc'
    MAP_SIZE = len(MAP_MARKS[0]), len(MAP_MARKS[1])
    SIGNS = {0: ' ', 1: 'X', 2: 'O'}

    def __init__(self, first_player, second_player):
        self.is_X_turn = True
        self.area = {num + char: 0 for num in Area.MAP_MARKS[0] for char in Area.MAP_MARKS[1]}
        self.players = {1: first_player, 2: second_player}

    def display(self):
        area_text = f'--{"--".join(list(Area.MAP_MARKS[1].upper()))}--\n'
        for row in Area.MAP_MARKS[0]:
            area_text += row
            for col in Area.MAP_MARKS[1]:
                area_text += f'[{Area.SIGNS[self.area[row + col]]}]'
            area_text += '\n'
        area_text += '-' * (5 + 3 * (Area.MAP_SIZE[1] - 1))
        print(area_text)

    @staticmethod
    def input_validate(text):
        if len(text) != 2:
            raise ValueError('неверная длина строки. Пример: 1a или c3')
        text = text.lower()
        if text[0] in Area.MAP_MARKS[1] and text[1] in Area.MAP_MARKS[0]:
            return f'{text[1]}{text[0]}'
        elif text[0] in Area.MAP_MARKS[0] and text[1] in Area.MAP_MARKS[1]:
            return text
        else:
            raise ValueError('неверный символ')

    def action_handler(self):

        current_turn_code = 1 if self.is_X_turn else 2
        coord = input(f'{self.players[current_turn_code]} ход: ')
        coord = self.input_validate(coord)
        self.area[coord] = current_turn_code
        self.is_X_turn = not self.is_X_turn

    def _get_player_by_sign(self, sign):
        return self.players[sign] if sign != 0 else None

    def is_end_game(self):
        first_num = Area.MAP_MARKS[0][0]
        first_char = Area.MAP_MARKS[1][0]
        last_num = Area.MAP_MARKS[0][-1]
        for num in Area.MAP_MARKS[0]:
            if all(self.area[num + char] == self.area[num + first_char] != 0 for char in Area.MAP_MARKS[1]):
                return Area.SIGNS[self.area[num + first_char]], self._get_player_by_sign(self.area[num + first_char])

        for char in Area.MAP_MARKS[1]:
            if all(self.area[num + char] == self.area[first_num + char] != 0 for num in Area.MAP_MARKS[0]):
                return Area.SIGNS[self.area[first_num + char]], self._get_player_by_sign(self.area[first_num + char])

        if all(self.area[num + char] == self.area[first_num + first_char] != 0
               for i, num in enumerate(Area.MAP_MARKS[0])
               for j, char in enumerate(Area.MAP_MARKS[1]) if i == j):
            return Area.SIGNS[self.area[first_num + first_char]], \
                   self._get_player_by_sign(self.area[first_num + first_char])

        if all(self.area[num + char] == self.area[last_num + first_char] != 0
               for i, num in enumerate(Area.MAP_MARKS[0])
               for j, char in enumerate(Area.MAP_MARKS[1]) if i + j == Area.MAP_SIZE[0]-1):
            return Area.SIGNS[self.area[last_num + first_char]], \
                   self._get_player_by_sign(self.area[last_num + first_char])

        if all(cell != 0 for cell in self.area.values()):
            return 'draw', None

        return None, None
