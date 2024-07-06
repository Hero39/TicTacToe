# Name: Hero Brouwer
# Description: This program implements Tic-Tac-Toe.
# https://www.youngwonks.com/blog/tic-tac-toe-python



def new_grid():
    grid = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    return grid


def create_grid(grid):
    for row in grid:
        print('|'.join(row))
        print('-' * 5)


# Checks the winner of the game
def check_winner(grid):
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] != ' ':
            return grid[i][0]
        elif grid[0][i] == grid[1][i] == grid[2][i] != ' ':
            return grid[0][i]
        elif grid[0][0] == grid[1][1] == grid[2][2] != ' ':
            return grid[2][2]
        elif grid[0][2] == grid[1][1] == grid[2][0] != ' ':
            return grid[1][1]

        if all(grid[i][j] != ' ' for i in range(3) for j in range(3)):
            return 'Tie'

        return None

def game(grid):
    playing = True
    field_completion = grid

    list_rows = []
    list_cols = []
    player_1 = True

    turn = "Player 1"

    print("Welcome to Tic Tac Toe")

    if player_1:
        turn = "Player 1"
    else:
        turn = "Player 2"
    print(f"{turn} needs to make a move")


    while playing:
        print(field_completion)
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))

        # Check if input is valid row
        if 0 <= row <= 2 and 0 <= col <= 2 and field_completion[row][col] == ' ':
                print(row, col)

                if player_1:
                    # Draw 'X' on flied
                    grid[row][col] = 'X'
                    player_1 = False
                else:
                    # Draw 'O' on field
                    grid[row][col] = 'O'
                    player_1 = True
        else:
            print(f"Invalid input: row = {row} and col = {col} ")

        if check_winner(field_completion) != None:
            playing = False

    if playing == False:
        winner = check_winner(field_completion)
        if winner == 'X':
            print("Player X won the game!")
        elif winner == 'O':
            print("Player O won the game!")
        else:
            print("It was a tie!")

def main():
    grid = new_grid()
    create_grid(grid)
    game(grid)
    new_round = input("Play again (Y/N)").upper()

    while new_round == "Y":
        grid = create_grid()
        game(grid)

if __name__ == "__main__":
    main()