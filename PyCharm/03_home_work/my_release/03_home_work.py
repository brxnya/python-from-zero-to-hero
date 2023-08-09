import random


class InitGame:
    def __init__(self):
        self.alphabet = {
            'а': 'а', 'б': 'б', 'в': 'в', 'г': 'г', 'д': 'д', 'е': 'е', 'ж': 'ж', 'з': 'з', 'и': 'и', 'й': 'й',
            'к': 'к', 'л': 'л', 'м': 'м', 'н': 'н', 'о': 'о', 'п': 'п', 'р': 'р', 'с': 'с', 'т': 'т', 'у': 'у',
            'ф': 'ф', 'х': 'х', 'ц': 'ц', 'ч': 'ч', 'ш': 'ш', 'щ': 'щ', 'ъ': 'ъ', 'ы': 'ы', 'ь': 'ь', 'э': 'э',
            'ю': 'ю', 'я': 'я',
        }
        self.get_len_for_generate_word = int(input('Укажите длину слова:\n'))
        self.get_available_mistakes = int(input('Число допустимых ошибок:\n'))
        self.get_letter = None
        self.word = None
        self.hidden_word = None


class Hangman(InitGame):
    def generate_word(self) -> str:
        with open('WordsStockRus.txt', 'r', encoding='utf-8') as file:
            words = file.readlines()
            sorted_words = []
            for index, value in enumerate(words):
                if len(value) == self.get_len_for_generate_word + 1:
                    sorted_words.append(value.strip('\n'))
            return random.choice(sorted_words)

    def show_tries_for_mistake(self):
        print(f'\nОсталось попыток: {self.get_available_mistakes}')

    def show_letters_open_or_hidden(self):
        print('\n\tДоступные буквы:')
        for i, v in enumerate(self.alphabet):
            if (i + 1) % 16 == 0:
                print(f'{self.alphabet[v]}')
            else:
                print(f'{self.alphabet[v]}|', end='')

    def show_letters_already_named(self):
        for i, v in enumerate(self.hidden_word):
            if (i + 1) % len(self.hidden_word) == 0:
                print(f'{v}')
            else:
                print(f'{v}|', end='')

    def user_input(self):
        self.get_letter = input('\nБуква?\n')

    def game(self):
        self.word = self.generate_word()
        self.hidden_word = len(self.word) * '_'
        print('\t\tИгра началась!!!\n')
        while self.get_available_mistakes != 0:
            flag = 0
            self.show_letters_already_named()
            self.user_input()
            print(f'\nВы ввели букву: [{self.get_letter}]')
            lst = list(self.hidden_word)
            for k, v in enumerate(self.word):
                if v == self.get_letter:
                    lst[k] = self.get_letter
                    self.hidden_word = ''.join(lst)
                    flag += 1
            self.show_letters_already_named()
            if self.hidden_word == self.word:
                print('ВЫ ПОБЕДИЛИ!')
                break
            self.alphabet[self.get_letter] = '_'
            self.show_letters_open_or_hidden()
            if flag == 0:
                self.get_available_mistakes -= 1
            self.show_tries_for_mistake()
        if self.get_available_mistakes == 0:
            print(f'ВЫ ПРОИГРАЛИ!\nЗагаданное слово было: {self.word}')


if __name__ == '__main__':
    Hangman().game()
