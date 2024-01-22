import random

def create_grid(width, height):
    return [[random.choice([0, 1]) for _ in range(width)] for _ in range(height)]

def display_grid(grid):
    for row in grid:
        print(''.join('#' if cell else ' ' for cell in row))

def count_neighbors(grid, x, y):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if 0 <= x + i < len(grid) and 0 <= y + j < len(grid[0]):
                count += grid[x + i][y + j]
    return count

def update_grid(grid):
    new_grid = create_grid(len(grid[0]), len(grid))
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            neighbors = count_neighbors(grid, i, j)
            if cell:
                new_grid[i][j] = 1 if neighbors in [2, 3] else 0
            else:
                new_grid[i][j] = 1 if neighbors == 3 else 0
    return new_grid
