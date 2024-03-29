import random

def create_grid(width, height, pattern=None):
    if pattern is None:
        return [[random.choice([0, 1]) for _ in range(width)] for _ in range(height)]
    else:
        return [[pattern(x, y) for x in range(width)] for y in range(height)]

def display_grid(grid):
    for row in grid:
        print(''.join('#' if cell else ' ' for cell in row))

def count_neighbors(grid, x, y):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0 or not (0 <= x + i < len(grid) and 0 <= y + j < len(grid[0])):
                continue
            count += grid[x + i][y + j]
    return count

def update_grid(grid):
    new_grid = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            neighbors = count_neighbors(grid, i, j)
            if cell:
                new_grid[i][j] = 1 if neighbors in [2, 3] else 0
            else:
                new_grid[i][j] = 1 if neighbors == 3 else 0
    return new_grid

def main():
    width, height = 10, 10  # Grid size
    grid = create_grid(width, height)

    for _ in range(5):  # Run for a fixed number of iterations for demonstration
        display_grid(grid)
        grid = update_grid(grid)
        input("Press Enter to continue...")

if __name__ == "__main__":
    random.seed(42)  # Optional: for reproducibility
    main()

