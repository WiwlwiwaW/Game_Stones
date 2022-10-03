import random

while True:
    xod = 1
    N = random.randint(4, 30)
    name1 = input('Введите имя 1-ого игрока:\n')
    name2 = input('Введите имя 2-ого игрока:\n')
    n = random.randint(1, 2)
    if n == 1:
        print(f'Первый ход делает: {name1}\n')
        one = name1
        two = name2
    else:
        print(f'Первый ход делает: {name2}\n')
        one = name2
        two = name1
    while N > 0:
        if xod == 1:
            while True:
                try:
                    k = int(input(f'Текущее значение камней в куче: {N}\n'
                                  f'{one}, сколько камней вы хотите убрать? (1, 2 или 3)\n'))
                    if k > 3 or k < 1:
                        print('Нужно убрать как минимум 1 камень, но не больше 3')
                    else:
                        N -= k
                        xod += 1
                        break
                except ValueError:
                    print('Вы ввели не число')
        else:
            while True:
                try:
                    k = int(input(f'Текущее значение камней в куче: {N}\n'
                                  f'{two}, сколько камней вы хотите убрать? (1, 2 или 3)\n'))
                    if k > 3 or k < 1:
                        print('Нужно убрать как минимум 1 камень, но не больше 3')
                    else:
                        N -= k
                        xod -= 1
                        break
                except ValueError:
                    print('Вы ввели не число')
    if xod == 1:
        print(f'{one} победил! Молодец!\n{two}, не расстраивайся это всего лишь игра.')
    if xod == 2:
        print(f'{two} победил! Молодец!\n{one}, не расстраивайся это всего лишь игра.')
    reset = input('Если хотите начать игру заново напишите: "да" иначе напишите что-нибудь другое\n')
    if reset != 'да' and reset != 'Да':
        exit()
