import random

class Table:

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.array = [[random.randint(1, 10)]*columns for i in range(rows)]

    def print(self):
        for i in range(self.rows):
            print(self.array[i], end='\n')
        print('\n')

    def get_value(self, row, column):
        if row >= self.rows or column >= self.columns:
            return None
        else: return self.array[row-1][column-1]

    def set_value(self, row, column, number):
        if row >= self.rows or column >= self.columns:
            print("Объект за пределами таблицы")
        else: 
            self.array[row-1][column-1] = number
            return self.array[row][column]

    def n_rows(self):
        return self.rows

    def n_cols(self):
        return self.columns

    def delete_row(self, row):
        self.array.pop(row-1)

    def delete_col(self, col):
        for i in range(self.rows):
                for j in range(self.columns):
                    if j == col-1:
                        self.array[i].pop(j)

    def add_row(self, row):
        if row > len(self.rows):
            print("Объект за пределами таблицы")
        else:
            self.array = self.array[0:row-1] + [[0]*self.columns] + self.array[row-1:]

    def add_col(self, col):
        if col > len(self.columns):
            print('Объект за пределами таблицы')
        else:
            for i in range(self.rows):
                self.array[i] = self.array[i][0:col-1] + [0] + self.array[i][col-1:]

test = Table(4, 6)
test.print()
test.add_col(2)
test.print()