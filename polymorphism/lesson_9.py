class TicTacToe():
    def __init__(self, level='easy'):
        self.field = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
# BEGIN (write your solution here)
        DIFFICULTIES = {'easy': Easy, 'normal': Normal}
        self.difficulty = DIFFICULTIES[level]

    def show_field(self):
        field = f'\n{"-" * 11}\n'.join(
            [
                '|'.join([f' {" " if s is None else s} ' for s in row])
                for row in self.field
            ]
        )
        print(field)

    def go(self, *values):
        if values:
            row = values[0]
            col = values[1]
            self.field[row][col] = 'X'
        else:
            pc_player = self.difficulty(self.field)
            row, col = pc_player.move()
            self.field[row][col] = 'O'
        return self.winning_move()

    def winning_move(self):
        for row in self.field:
            if row[0] == row[1] == row[2] is not None:
                return True
        rotated_field = [list(row) for row in zip(*self.field[::-1])]
        for row in rotated_field:
            if row[0] == row[1] == row[2] is not None:
                return True
        if self.field[0][0] == self.field[1][1] == self.field[2][2]\
            is not None or \
            rotated_field[0][0] == rotated_field[1][1] == rotated_field[2][2]\
                is not None:
            return True
        return False
# END


class Easy():
    # BEGIN (write your solution here)
    def __init__(self, field):
        self.field = field

    def move(self):
        for i, row in enumerate(self.field):
            for j, space in enumerate(row):
                if space is None:
                    print(i, j)
                    return i, j
    # END


class Normal():
    # BEGIN (write your solution here)
    def __init__(self, field):
        self.field = field

    def move(self):
        field = [[value for value in row] for row in reversed(self.field)]
        for i, row in enumerate(field):
            for j, space in enumerate(row):
                if space is None:
                    print(~i, j)
                    return ~i, j
    # END


game = TicTacToe('normal')
print(game.go(2, 2))
print(game.go())
print(game.go(1, 2))
print(game.go())
print(game.go(1, 0))
print(game.go())
game.show_field()
