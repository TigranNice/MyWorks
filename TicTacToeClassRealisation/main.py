import random


class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    def __init__(self):
        self.is_human_win = False
        self.is_computer_win = False
        self.is_draw = False

        self.pole = tuple((Cell(), Cell(), Cell()) for _ in range(3))

    def init(self):
        self.is_human_win = False
        self.is_computer_win = False
        self.is_draw = False

        self.pole = tuple((Cell(), Cell(), Cell()) for _ in range(3))

    def check_line(self, cells):
        val_cells = [cells[j].value for j in range(3)]
        if val_cells == [1, 1, 1]:
            self.is_human_win = True
            return "End"
        if val_cells == [2, 2, 2]:
            self.is_computer_win = True
            return "End"

        return "Continue"

    def game_check(self):
        for i in range(3):
            cells = self.pole[i]
            res = self.check_line(cells)
            if res == "End":
                return res
            cells = []
            for j in range(3):
                cells.append(self.pole[j][i])
            res = self.check_line(cells)
            if res == "End":
                return res

        cells = [self.pole[j][j] for j in range(3)]
        res = self.check_line(cells)
        if res == "End":
            return res

        cells = [self.pole[j][2 - j] for j in range(3)]
        res = self.check_line(cells)
        if res == "End":
            return res

        if self.check_full():
            self.is_draw = True
            return "End"

    def check_full(self):
        for i in range(3):
            for j in range(3):
                if bool(self.pole[i][j]) != 0:
                    return False
        return True

    def __bool__(self):
        if self.is_computer_win or self.is_human_win or self.is_draw:
            return False
        return True

    def __getitem__(self, item):
        row, col = item[0], item[1]
        self.check(row, col)
        return self.pole[row][col].value

    def __setitem__(self, item, value):
        if self.game_check() == "End":
            return
        self.check(item[0], item[1])
        if not bool(self.pole[item[0]][item[1]]):
            raise ValueError('клетка уже занята')
        self.pole[item[0]][item[1]].value = value
        self.game_check()

    def show(self):
        for i in self.pole:
            for j in i:
                print(j.value, end="|")
            print()
            print("------")

    def get_free_cell(self):
        for i in range(3):
            for j in range(3):
                if bool(self.pole[i][j]):
                    return self.pole[i][j]

    def get_random_cell(self):
        free_cell = []
        for i in range(3):
            for j in range(3):
                if bool(self.pole[i][j]):
                    free_cell.append(self.pole[i][j])
        return random.choice(free_cell)

    def human_go(self):
        if self.game_check() == "End":
            print(self.is_draw, self.is_human_win, self.is_computer_win)
            return
        cell = self.get_free_cell()
        cell.value = self.HUMAN_X

    def computer_go(self):
        if self.game_check() == "End":
            print("PP")
            return
        cell = self.get_random_cell()
        cell.value = self.COMPUTER_O

    @staticmethod
    def check(row, col):
        if not isinstance(row, int) or not isinstance(col, int):
            raise IndexError('некорректно указанные индексы')

        if ((row < 0) or (row > 2)) or ((col < 0) or (col > 2)):
            raise IndexError('некорректно указанные индексы')



class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        return True if self.value == 0 else False


#code for test

game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1


game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")
