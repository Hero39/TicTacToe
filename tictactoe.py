# Name: Hero Brouwer
# Description: This program implements Tic-Tac-Toe.
# For Future: Instead of two individual inputs, take one input which is a
# coordinate.



# Creates new empty grid for Tic Tac Toe
def new_grid():
    grid = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    return grid


# Creates the grid and the lines
def create_grid(grid):
    for row in grid:
        print('|'.join(row))
        print('-' * 5)


# Checks the winner of the game
def check_winner(grid):
    for i in range(3):
        # Check rows and columns
        if grid[i][0] == grid[i][1] == grid[i][2] != ' ':
            return grid[i][0]
        elif grid[0][i] == grid[1][i] == grid[2][i] != ' ':
            return grid[0][i]

        # Check diagonals
        elif grid[0][0] == grid[1][1] == grid[2][2] != ' ':
            return grid[2][2]
        elif grid[0][2] == grid[1][1] == grid[2][0] != ' ':
            return grid[1][1]

        if all(grid[i][j] != ' ' for i in range(3) for j in range(3)):
            return 'Tie'

    return None


# def check_input(row, col):


def print_winner(winner):
    if winner == 'X':
        print("Player X won the game!")
    elif winner == 'O':
        print("Player O won the game!")
    else:
        print("It was a tie!")


# The game
def game(grid):
    playing = True
    field = grid
    player_1 = True

    print("Welcome to Tic Tac Toe")

    while playing:
        create_grid(field)

        if player_1:
            print("Player 1 needs to make a move")
        else:
            print("Player 2 needs to make a move")

        print("Give an coordinate of a field (0-2) where.")
        print("Row and column are seperated by a comma.")
        print("Example: (1,2 symbolizes the field in row 1 and column 2.")
        row_str, col_str, *_ = input("Enter row and column (0-2): ").split(",")

        # Check if input is valid field
        try:
            row = int(row_str)
            col = int(col_str)

            if 0 <= row <= 2 and 0 <= col <= 2 and field[row][col] == ' ':

                    if player_1:
                        # Draw 'X' on flied
                        grid[row][col] = 'X'
                        player_1 = False
                    else:
                        # Draw 'O' on field
                        grid[row][col] = 'O'
                        player_1 = True

            else:
                print(f"Values too high/too low: row = {row} and col = {col} ")
        except:
            print(f"Error: row = {row_str} & col = {col_str} ")

        winner = check_winner(field)

        if winner is not None:
            playing = False

    create_grid(field)

    print_winner(winner)

def main():
    grid = new_grid()
    game(grid)
    new_round = input("Play again (Y/N)").upper()

    while new_round == "Y":
        grid = new_grid()
        game(grid)
        new_round = input("Play again (Y/N)").upper()


if __name__ == "__main__":
    main()