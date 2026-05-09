import os

def clear_terminal():
    """
    Clears the terminal screen
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

        
def display_board(board):
    """
    Clears the terminal and renders a 3x3 game board.

    Args:
        board (list[list[str]]): A 2D list (3X3) containing the current state of the game.
    """
    clear_terminal()

    for i in range(3):
        for j in range(3):
            if j < 2:
                print(f" {board[i][j]} ",end='|')
            else:
                print(f" {board[i][j]} ")
        if i < 2:
            print('-----------')


def player_input():
    """
    Assign markers to the players of the game

    Returns:
           tuple: A pair of strings in the format (player1_marker, player2_marker)
    """
    marker = ''
    while not(marker == 'X' or marker == 'O'):
        marker = input("Player 1 please select your marker X or O\n").strip().upper()
        clear_terminal()

    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return (player1,player2)


def play_move(board,player):
    """
    Prompts the user to select a board position and update the board in-place

    Args:
        board (list[list[str]]): A 2D list (3X3) containing the current state of the game.
        player (str): The symbol of the current player.
    """
    while True:
        pos = input('\nEnter a position\n')

        if not pos.isdigit() or not (1 <= int(pos) <= 9):
            print("Invalid input, please enter a number between 1 and 9")
            continue

        #Convert 1-based input to 0-based index 
        pos = int(pos) - 1
        row = pos//3
        col = pos%3

        if board[row][col] != ' ':
            print("Position is already taken!")
            continue
        
        #Update the board and exit the loop
        board[row][col] = player
        break


def status(board):
    """
    Evaluates the current state of the board to determine if there is a winner,a draw, or if the game should continue.

    Args:
        board (list[list[str]]): A 3x3 2D list representing the game board.

    Returns:
        str|int: Returns the winning marker ('X' or 'O') if a player has won.
                 Returns -1 if the game is a draw (board is full with no winner).
                 Returns 0 if the game is still in progress.
    """
    # Check rows and columns
    for i in range(3):
        # Rows
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        # Columns
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    # Check for draw (if no spaces left)
    if all(cell != ' ' for row in board for cell in row):
        return -1

    return 0


def main():
    player1, player2 = player_input()
    player = player1
    board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

    while True:
        play_move(board,player)
        display_board(board)
        if player == player1:
            player = player2
        else:
            player = player1
        result = status(board)
        if result == 0:
            continue

        if result == 'X':
            if player1 == 'X':
                print('\nplayer 1 wins')
            else:
                print('\nplayer 2 wins')
        elif result == 'O':
            if player1 == 'O':
                print('\nplayer 1 wins')
            else:
                print('\nplayer 2 wins')
        else:
            print('its a draw')
        break

if __name__ == "__main__":
    main()