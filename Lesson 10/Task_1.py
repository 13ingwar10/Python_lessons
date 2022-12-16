class MinStat:

    def __init__(self):
        self.array = []
        self.output = 0

    def add_number(self):
        self.array = list(map(int, input("Введите число или последовательность через пробел: \n").split()))
        return self.array

    def result(self):

        if len(self.array) != 0:
            self.array.sort()
            self.output = self.array[0]
            return self.output
        else: return None


    def print(self):
        print(self.array)
        print(self.output)

class MaxStat:

    def __init__(self):
        self.array = []
        self.output = 0

    def add_number(self):
        self.array = list(map(int, input("Введите число или последовательность через пробел: \n").split()))
        return self.array

    def result(self):

        if len(self.array) != 0:
            self.array.sort()
            self.output = self.array[-1]
            return self.output
        else: return None

    def print(self):
        print(self.array)
        print(self.output)

class Average:

    def __init__(self):
        self.array = []
        self.output = 0

    def add_number(self):
        self.array = list(map(int, input("Введите число или последовательность через пробел: \n").split()))
        return self.array

    def result(self):

        if len(self.array) != 0:
            counter = 0
            for element in self.array:
                counter += element
            self.output = round(float(counter / len(self.array)),7)
            return self.output
        else: return None

    def print(self):
        print(self.array)
        print(self.output)

test = Average()
test.add_number()
test.result()
test.print()
