class GameLogic:
    def __init__(self):
        self.current_player = 1
        self.grid = [[None for _ in range(4)] for _ in range(4)]

    def make_move(self, row, col):
        if self.grid[row][col] is None:
            self.grid[row][col] = self.current_player
            self.current_player = 2 if self.current_player == 1 else 1
            return True
        return False

    def check_win(self):
        for row in self.grid:
            if all(cell == row[0] and cell is not None for cell in row):
                return True

        for col in range(4):
            if all(self.grid[row][col] == self.grid[0][col] and self.grid[row][col] is not None for row in range(4)):
                return True

        if all(self.grid[i][i] == self.grid[0][0] and self.grid[i][i] is not None for i in range(4)):
            return True

        if all(self.grid[i][3 - i] == self.grid[0][3] and self.grid[i][3 - i] is not None for i in range(4)):
            return True

        return False