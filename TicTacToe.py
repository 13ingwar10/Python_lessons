import random

class TicTacToeBoard:

    def __init__(self):
        self.field =  list(range(1, 10))
        self.player = 1
        self.token = ''
        self.game_over = False

    def new_game(self):

        print("Добро пожаловать в игру!")
        print("Определим право первого хода! Вы по очереди будете пытаться угадать число на шестигранном кубике, победитель ходит первым")
        self.first_move()
        self.token = 'X'
        self.game_over = False

        while (self.game_over == False):
            self.field = self.PlayerMove()
            self.game_over = self.check_field()

            if self.player == 1:
                self.player = 2
            else: self.player = 1

            if self.token == "X":
                self.token = "O"
            else: self.token = "X"


    def get_field(self):
        for i in range(0, 3):
            print(self.field[0 + i*3], "|" ,self.field[1 + i*3], "|" , self.field[2 + i*3])

    def first_move(self):
        self.player = 1
        number = 1
        dice = 0

        while (number != dice):
            number = int(input("Введите число от 1 до 6: "))
            while (number < 1 or number > 6):
                number = int(input("Ошибка! Введите число от 1 до 6: "))
            dice = random.randint(1, 6)

            if (number == dice):
                    print(f"Вы угадали! Игрок №{self.player} ходит первым!")
            elif self.player == 1:
                self.player = 2
            else:
                self.player = 1

        return self.player

    def check_field(self):

        for i in range(0, 9, 3):
            if self.field[i] == self.field[i+1] == self.field[i+2] == self.token:
                print(f"Игрок №{self.player} выиграл!")
                self.game_over = True

        for i in range(3):
            if self.field[i] == self.field[i+3] == self.field[i+6] == self.token:
                print(f"Игрок №{self.player} выиграл!")
                self.game_over = True

        if (self.field[0] == self.field[4] == self.field[8] == self.token):
                print(f"Игрок №{self.player} выиграл!")
                self.game_over = True

        if (self.field[2] == self.field[4] == self.field[6] == self.token):
                print(f"Игрок №{self.player} выиграл!")
                self.game_over = True
        
        return self.game_over

    def PlayerMove(self):
    
        self.get_field()

        move = input(f"Ход игрока {self.player}. На какое поле вы хотите поставить " + self.token + "?  ")

        while(int(move) < 1 or int(move) > 9 or str(self.field[int(move) - 1]) in "XO"):
            move = input("Ошибка! введите число от 1 до 9 в незанятое поле ")

        self.field[int(move) - 1] = self.token
        return self.field

board = TicTacToeBoard()
board.new_game()