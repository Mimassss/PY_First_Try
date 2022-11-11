
print("Укажите имя первого игрока")
FirstPlayer = input()
print("\n")



print("Укажите имя второго игрока")
SecondPlayer = input()
print("\n")


while Currentplayer == FirstPlayer:
    print(Currentplayer, "Крестик или Нолик")
    print("Нажмите 1 для выбора X")
    print("Нажмите 2 для выбора O")

the_choice = input()

    if the_choice == 1:
        playerchoice['X'] = Currentplayer
        if Currentplayer == FirstPlayer:
            playerchoice['O'] = SecondPlayer
        else:
            playerchoice['O'] = FirstPlayer

        elif the_choice == 2:
        playerchoice['O'] = Currentplayer

        if Currentplayer == FirstPlayer:
            playerchoice['X'] = SecondPlayer

        else:
            playerchoice['X'] = FirstPlayer
            
        else:
            if the_choice != 1:
                print('Попробуйте еще раз')
        else:
        if the_choice != 2:
            print('Попробуйте еще раз')

    elif the_choice == 3:
        print('Игра окончена')
        break





Currentplayer = FirstPlayer

# Как теперь не спрашивать каждый ход кем играет текущий игрок?




def xofield(val):"""Функция рисования поля"""
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(val[0], val[1], val[2]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(val[3], val[4], val[5]))
    print('\t_____|_____|_____')

    print("\t     |     |")

    print("\t  {}  |  {}  |  {}".format(val[6], val[7], val[8]))
    print("\t     |     |")
    print("\n")
    ...


def check_vic(playerposition, Currentplayer):
    """Перечесление комбинаций для победы"""
    solution = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    """Проверка, получена или нет выйграшная комбинация"""
    for i in solution:
        if all(j in playerposition[Currentplayer] for j in i):
            """Если на поле есть выйграшная комбинация - Tru"""
            return True
        else:
            return False


def check_tie(playerposition): """Проверяем ничью по сумме занятых клеток"""
    if len(playerposition['X']) + len(playerposition['O']) == 9:
        return True
    else:
        return False

