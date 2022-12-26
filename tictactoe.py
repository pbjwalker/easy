# This is the first milestone project in the Python bootcamp.
# It was designed to run in a Jupyter Notebook cell.
# If you want to run this outside of a Jupyter Notebook,
# Comment out the import line, and the call to the clear_output() method.

from IPython.display import clear_output
from random import randint


# Player 1 chooses to be X or O
def player_input():
    marker = ''
    
    # keep asking player 1 to choose X or O
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, do you want to be (X or O)?  ')
    
    # then assign player 2 the opposite marker
    player1 = marker
    
    if marker == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return (player1,player2)  # use tuple unpacking on the result



# Randomly decide who goes first
# I don't like the game like this, but it's what the course wanted.
def choose_first():
    num = randint(1,3)
    if num == 1:
        return 'Player 1'
    else:
        return 'Player 2'


# Displays the board
def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])
    

# Checks if a position on the board has already been played
def space_check(board, position):
    if board[position] != 'X' and board[position] != 'O':
        return True
    else:
        return False  


# Takes the player's choice, checks that it's in the valid move range, and checks if it's already played
def player_choice(board):    
    choice = 'wrong'
    possible = ['1','2','3','4','5','6','7','8','9']
    
    while True:
        while choice not in possible:
            choice = input('Enter your next move (1-9): ')

        if space_check(board,int(choice)):
            break
        else:
            print("That position is filled.")
            choice = 'wrong'
    
    return int(choice)


# Check if there's a win
def win_check(board, mark):
    if (board[7] == board[8] == board[9] == mark) or (board[4] == board[5] == board[6] == mark) or (board[1] == board[2] == board[3] == mark):
        print(f'{mark} wins with 3 in a row!')
        return True
    elif (board[7] == board[4] == board[1] == mark) or (board[8] == board[5] == board[2] == mark) or (board[9] == board[6] == board[3] == mark):
        print(f'{mark} wins with 3 in a column!')
        return True
    elif (board[7] == board[5] == board[3] == mark) or (board[8] == board[5] == board[1] == mark):
        print(f'{mark} wins with 3 diagonally!')
        return True
    else:
        return False
    

# Check if the board is full
def full_board_check(board):
    for item in board:
        # So if it's not an X, O or a #, then there's at least one available space
        if item != 'X' and item != 'O' and item != '#':
            return False
    return True


# Do you want to play again?
def replay():
    choice = 'wrong'
    
    while choice != 'y' and choice != 'n':
        choice = input('Do you want to play again? (y/n): ')
    if choice == 'y':
        return True
    else:
        return False
    
    
##############################################


print('Welcome to Tic Tac Toe!')

while True:
    
    # A clean board
    # board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    board = ['#','1','2','3','4','5','6','7','8','9']
    
    # Player chooses to be X or O
    player1,player2 = player_input()
    
    # Computer decided who goes first
    goes_first = choose_first()
    if goes_first == "Player 1":
        toggle_player = True
    else:
        toggle_player = False
    
    # This starts the game
    game_on = True

    while game_on:
        display_board(board)
        
        # Player 1's turn
        if toggle_player:
            print('Player 1, your turn')
            mark = player1

        # Player2's turn.
        else:
            print('Player 2, your turn')
            mark = player2      
        
        # Player chooses a move, board is updated and displayed
        choice = player_choice(board)
        board[choice] = mark
        display_board(board)
        
        # Check for a win
        if win_check(board, mark):
            game_on = False
        else:
            # If the board is full, it's a tie
            if full_board_check(board):
                print("It's a tie!")
                game_on = False
        
        # Change player for next turn
        toggle_player = not toggle_player
    
    
    
    
    if not replay():
        break
