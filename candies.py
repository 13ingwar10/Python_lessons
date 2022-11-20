import random

def PlayTheGame():
    count = 300

    game_mode = (int(input("Выберите соперника: 1 - человек; 2 - компьютер  ")))

    if (game_mode == 1):
        print("Определим право первого хода! Вы по очереди будете пытаться угадать число на шестигранном кубике, победитель ходит первым")
        player = FirstMove()
        while (count > 0):
            print(f"Конфет осталось {count}!")
            count = PlayerMoveMode1(count, player)
            VictoryCheckMode1(count, player)
            if player == 1:
                player = 2
            else:
                player = 1
    else:
        while (count > 0):
            print(f"Конфет осталось {count}!")
            count = PlayerMoveMode2(count)
            if VictoryCheckMode2(count): return print("Игрок победил!")
            count = AIMove(count)
            if VictoryCheckMode2(count): return print("AI победил :(")


def PlayerMoveMode1(count, player):
    number = int(input(f"Ход Игрока №{player}. Сколько взять конфет? (максимум 28) "))
    while(number < 0 or number > 28):
        number = int(input("Ошбика! Введите число от 0 до 28: "))
    count -= number
    return count

def PlayerMoveMode2(count):
    number = int(input(f"Ход Игрока. Сколько взять конфет? (максимум 28) "))
    while(number < 0 or number > 28):
        number = int(input("Ошибка! Введите число от 0 до 28: "))
    count -= number
    return count

def AIMove(count):

    if (count <= 28):
        number = count
    else:
        number = random.randint(1, 28)
    print(f"Ход AI. Взято конфет - {number}")
    count -= number
    return count

def VictoryCheckMode1(count, player):
    if count <= 0:
        return print(f"Игрок №{player} выиграл!")

def VictoryCheckMode2(count):
    if count <= 0:
        return True

def FirstMove():
    player = 1
    number = 1
    dice = 0

    while (number != dice):
        number = int(input("Введите число от 1 до 6 "))
        while (number < 1 or number > 6):
            number = int(input("Ошибка! Введите число от 1 до 6"))
        dice = random.randint(1, 6)

        if (number == dice):
                print(f"Вы угадали! Игрок №{player} ходит первым!")
        elif player == 1:
            player = 2
        else:
            player = 1

    return player

PlayTheGame()