import random

def create_grid(width, height):
    return [[random.choice([0, 1]) for _ in range(width)] for _ in range(height)]

def display_grid(grid):
    for row in grid:
        print(''.join('#' if cell else ' ' for cell in row))
