import random

def PlayTheGame():
    deck =  list(range(1, 10))
    print("Определим право первого хода! Вы по очереди будете пытаться угадать число на шестигранном кубике, победитель ходит первым")
    player = FirstMove()
    token = "X"
    game_over = False


    while (game_over == False):
        deck = PlayerMove(deck, player, token)
        game_over = CheckWin(deck, player, token, game_over)

        if player == 1:
            player = 2
        else: player = 1

        if token == "X":
            token = "O"
        else: token = "X"

def PrintDeck(deck):
    for i in range(0, 3):
        print(deck[0 + i*3], "|" ,deck[1 + i*3], "|" , deck[2 + i*3])

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

def PlayerMove(deck, player, token):
    
    PrintDeck(deck)

    move = input(f"Ход игрока {player}. На какое поле вы хотите поставить " + token + "?  ")

    while(int(move) < 1 or int(move) > 9 or str(deck[int(move) - 1]) in "XO"):
        move = input("Ошибка! введите число от 1 до 9 в незанятое поле ")

    deck[int(move) - 1] = token
    return deck
    

def CheckWin(deck, player, token, game_over):

    game_over = False

    for i in range(0, 9, 3):
        if deck[i] == deck[i+1] == deck[i+2] == token:
            print(f"Игрок №{player} выиграл!")
            game_over = True

    for i in range(3):
        if deck[i] == deck[i+3] == deck[i+6] == token:
            print(f"Игрок №{player} выиграл!")
            game_over = True

    if (deck[0] == deck[4] == deck[8] == token):
            print(f"Игрок №{player} выиграл!")
            game_over = True

    if (deck[2] == deck[4] == deck[6] == token):
            print(f"Игрок №{player} выиграл!")
            game_over = True
    
    return game_over


PlayTheGame()