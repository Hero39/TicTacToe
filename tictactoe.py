# Name: Hero Brouwer
# Description: This program implements Tic-Tac-Toe.


grid = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]


def create_grid():
    for row in grid:
        print('|'.join(row))
        print('-' * 5)

create_grid()