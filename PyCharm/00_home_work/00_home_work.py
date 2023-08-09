import random


def randoms(val_min, val_max):
    while True:
        yield random.randint(val_min, val_max)


rand_num = randoms(1, 50)
n = next(rand_num)

i = 0
for _ in range(6):
    us_num = int(input(f'Я загадал число от 1 до 50, попробуй угадать! Осталось {6 - _} попыток:\n'))
    if us_num > n:
        print(f'Загаданное число меньше, чем вы указали!')
        i += 1
    elif us_num < n:
        print(f'Загаданное число больше, чем вы указали!')
        i += 1
    else:
        print(f'Поздравляю! Вы угадали загаданное число! Это и в правду {n}!')
        break
if i == 6:
    print(f'Увы, вы проиграли :( Загаданное число {n}')
