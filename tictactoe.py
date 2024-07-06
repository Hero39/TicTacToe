# Name: Hero Brouwer
# Description: This program implements Tic-Tac-Toe.


grid = [
    ['_', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]


def create_grid():

    indices_rows = [i for i, x in enumerate(grid)]
    print(indices_rows)
    for row in grid:
        print('|'.join(row))
        print('-' * 5)

# def move_in_grid(x, y):
    
    
# def move_with_key():

create_grid()


def game():
    playing = True
    
    
    