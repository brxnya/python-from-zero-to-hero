class CreateTicTacToe:
    def __init__(self):
        self.index = {0: '_', 1: '_', 2: '_', 3: '_', 4: '_', 5: '_', 6: '_', 7: '_', 8: '_'}
        self.char = 'X'
        self.win = False

    def print_game_result(self):
        return (f'\t{self.index[0]}{self.index[1]}{self.index[2]}' + '\n' +
                f'\t{self.index[3]}{self.index[4]}{self.index[5]}' + '\n' +
                f'\t{self.index[6]}{self.index[7]}{self.index[8]}')


class Game(CreateTicTacToe):
    def win_combinations(self, check_char):
        if self.index[0] == check_char and self.index[1] == check_char and self.index[2] == check_char or\
                self.index[3] == check_char and self.index[4] == check_char and self.index[5] == check_char or\
                self.index[6] == check_char and self.index[7] == check_char and self.index[8] == check_char or\
                self.index[0] == check_char and self.index[4] == check_char and self.index[8] == check_char or\
                self.index[6] == check_char and self.index[4] == check_char and self.index[2] == check_char or\
                self.index[0] == check_char and self.index[3] == check_char and self.index[6] == check_char or\
                self.index[1] == check_char and self.index[4] == check_char and self.index[7] == check_char or\
                self.index[2] == check_char and self.index[5] == check_char and self.index[8] == check_char:
            return True
        else:
            return False

    def switch_char(self):
        if self.char == 'X':
            self.char = 'O'
        else:
            self.char = 'X'

    def checking_empty_cells(self):
        check_sum = 0
        for k, v in self.index.items():
            if v == '_':
                check_sum += 1
        if check_sum == 0:
            return False
        else:
            return True

    def start_game(self):
        print('TicTacToe')
        while self.win is False:
            if self.checking_empty_cells() is False:
                break
            user_choice = int(input('\nSelect index:\n'))
            if 0 <= user_choice <= 8 and self.index[user_choice] == '_':
                self.index[user_choice] = self.char
            else:
                print('Wrong index, try again')
                continue
            self.win = self.win_combinations(self.char)
            self.switch_char()
            print(self.print_game_result())
        print('Game over!')


if __name__ == '__main__':
    Game().start_game()
