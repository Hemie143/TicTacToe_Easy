from random import randint, choice
from copy import deepcopy


class Player:

    def __init__(self, level, symbol):
        self.level = level
        self.symbol = symbol

class UserPlayer(Player):

    valid_coords = ["1", "2", "3"]

    def play(self, grid):
        while True:
            move = input("Enter the coordinates:")
            if " " not in move:
                print("You should enter numbers!")
                continue
            else:
                x, y = move.split()
            if not x.isnumeric() and not y.isnumeric():
                print("You should enter numbers!")
            elif x not in self.valid_coords or y not in self.valid_coords:
                print("Coordinates should be from 1 to 3!")
            elif grid.read_cell(3 - int(y), int(x) - 1) in "XO":
                print("This cell is occupied! Choose another one!")
            else:
                # Turns
                # cells[3 - int(y)][int(x) - 1] = player[turn % 2]
                grid.write_cell(3 - int(y), int(x) - 1, self.symbol)
                break

class Grid:

    lines = [([0, 0], [0, 1], [0, 2]), ([1, 0], [1, 1], [1, 2]), ([2, 0], [2, 1], [2, 2]),
             ([0, 0], [1, 0], [2, 0]), ([0, 1], [1, 1], [2, 1]), ([0, 2], [1, 2], [2, 2]),
             ([0, 0], [1, 1], [2, 2]), ([2, 0], [1, 1], [0, 2])
             ]

    all_moves = [(0, 0), (1, 0), (2, 0),
                 (0, 1), (1, 1), (2, 1),
                 (0, 2), (1, 2), (2, 2)]

    def __init__(self):
        self.cells = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.state = None

    def init_grid(self):
        self.cells = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def read_cell(self, x, y):
        return self.cells[x][y]

    def print_grid(self):
        print("---------")
        for y in range(0, 3):
            grid_line = ' '.join(self.cells[y])
            print(f'| {grid_line} |')
        print("---------")

    def get_state(self):
        x_count = self.cells[0].count('X') + self.cells[1].count('X') + self.cells[2].count('X')
        o_count = self.cells[0].count('O') + self.cells[1].count('O') + self.cells[2].count('O')
        if abs(x_count - o_count) > 1:
            self.state = 'Impossible'
            return self.state

        empty_cell = any([cell == "_" for row in self.cells for cell in row])
        x3, o3 = False, False
        for coords in self.lines:
            line = [self.cells[x][y] for x, y in coords]
            x3 = x3 or all([c == 'X' for c in line])
            o3 = o3 or all([c == 'O' for c in line])
        if not x3 and not o3:
            if empty_cell:
                self.state = 'Game not finished'
            else:
                self.state = 'Draw'
        elif x3 and not o3:
            self.state = 'X wins'
        elif o3 and not x3:
            self.state = 'O wins'
        else:
            self.state = 'Impossible'
        return self.state

    def eval(self, symbol):
        for coords in self.lines:
            if all([self.cells[x][y] == symbol for x, y in coords]):
                return True
        return False

    def input(self):
        grid_input = input('Enter cells: ')
        for i, s in enumerate(grid_input):
            self.cells[i // 3][i % 3] = s

class TicTacToe:

    # numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    def __init__(self):
        self.playerX = None
        self.playerO = None
        self.grid = Grid()

    @staticmethod
    def get_player(level, symbol):
        if level == 'user':
            return UserPlayer(level, symbol)
        elif level == 'easy':
            return AIEasyPlayer(level, symbol)
        elif level == 'medium':
            return AIMediumPlayer(level, symbol)
        elif level == 'hard':
            return AIHardPlayer(level, symbol)

    def run(self):
        self.grid.print_grid()
        while not self.grid.win:
            for player in [self.playerX, self.playerO]:
                player.play(self.grid)
                self.grid.print_grid()
                self.grid.get_state()
                if 'play' not in self.grid.state:
                    print(self.grid.state)
                if self.grid.win:
                    break

    def run_menu(self):
        while True:
            print('Input command:')
            command = input()
            if command == 'exit':
                exit()
            if command.startswith('start') and command.count(' ') == 2:
                _, levelX, levelO = command.split(' ')
                self.playerX = self.get_player(levelX, 'X')
                self.playerO = self.get_player(levelO, 'O')
                self.grid.init_grid()
                self.run()
            else:
                print('Bad parameters!')
            exit()


game = TicTacToe()
game.run_menu()

