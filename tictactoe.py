# Name: Hero Brouwer
# Description: This program implements Tic-Tac-Toe.


grid = [
    [' ', ' ', ' '],
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


def game(grid):
    playing = True
    
    list_rows = []
    list_cols = []
    player_1 = True
    player_2 = False

    while playing:
        create_grid()
        row = input("enter row (0-2): ")

        if row >= 0 and row <= 2:
            col = input("enter column (0-2): ")
            if col >= 0 and col <= 2:
                rows_fields = [*grid]
                fields = [*rows_fields]
                
                player_1 = False
        else:
            print("Please enter an valid row")
            

def main():
    game(grid)

    new_round = input("Play again (Y/N)").upper()

    while new_round == "Y":
        game(grid)

if __name__ == "__main__":
    main()