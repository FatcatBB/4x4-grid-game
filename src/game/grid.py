class Grid:
    def __init__(self):
        self.grid = self.initialize_grid()

    def initialize_grid(self):
        return [[0 for _ in range(4)] for _ in range(4)]

    def display_grid(self):
        for row in self.grid:
            print(" | ".join(str(num) for num in row))
            print("-" * 21)