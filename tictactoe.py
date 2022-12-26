# This is the first milestone project in the Python bootcamp.
# It was designed to run in a Jupyter Notebook cell.
# If you want to run this outside of a Jupyter Notebook,
# Comment out the import line, and all of the calls to the clear_output() method.


# This lets us clear the board in Jupyter Notebook
from IPython.display import clear_output


# Player 1 chooses to be X or O
def player_choice():
    player1 = ''
    
    # keep asking player 1 to choose X or O until he makes a valid selection
    while player1 != 'X' and player1 != 'O':
        player1 = input('Player 1, do you want to be (X or O)?  ')
    
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    print(f'Player 1 = {player1}, Player 2 = {player2}')
    return (player1,player2)  # use tuple unpacking on the result


# Clear output and display the current board
def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])


# Player selects the location to place his mark
def player_input(valid_moves):
    choice = 'wrong'
    while choice not in valid_moves:
        choice = input('Enter a move (1-9): ')
    return int(choice)

    
def place_marker(board, valid_moves, marker, position):    
    board[position] = marker
    # remove that move from valid_moves
    valid_moves.pop(valid_moves.index(str(position)))
    return (board,valid_moves)


def change_player(player1_turn):
    player1_turn = not player1_turn
    return player1_turn

# Is the board full? Then it's a draw!
def full_board_check(valid_moves):
    if len(valid_moves) > 1:
        keep_playing = True
    else:
        print("It's a draw!")
        keep_playing = False
    return keep_playing


# Did anyone win?
def check_won(board):
    
    # Check 3 in a row
    if (board[7] == board[8] == board[9]) or (board[4] == board[5] == board[6]) or (board[1] == board[2] == board[3]):
        won = True
        message = "You won! 3 in a row!"

    # Check 3 in a column
    elif (board[7] == board[4] == board[1]) or (board[8] == board[5] == board[2]) or (board[9] == board[9] == board[3]):
        won = True
        message = "You won! 3 in a column!"

    # Check 3 diagonally
    elif (board[7] == board[5] == board[3]) or (board[8] == board[5] == board[1]):
        won = True
        message = "You won! 3 diagonally!"

    else:
        won = False
        message = ""

    return (won, message)


# Play again?
def replay():
    choice = input('Enter (q) to quit, anything else to play again: ')
    if choice == 'q':
        return False
    else:
        return True


###############  MAIN BODY OF PROGRAM ###############

# The initial variables
# board = ['#','1','2','3','4','5','6','7','8','9']
# valid_moves = ['#','1','2','3','4','5','6','7','8','9']
# player1_turn = False
keep_playing = True

print('Welcome to Tic Tac Toe!')

while keep_playing:
    game_on = True # this needs to be inside the inner while loop, or it only works once
    won = False
    board = ['#','1','2','3','4','5','6','7','8','9']
    valid_moves = ['#','1','2','3','4','5','6','7','8','9']
    player1_turn = False
    
    # player1 chooses X or O, player2 gets the other marker
    player1, player2 = player_choice()
    if player1 == 'X':
        player1_turn = True
    
    display_board(board)


    while game_on:
        
        if player1_turn:
            # player1's turn
            # marker set for player1
            marker = player1
            
            # the player picks his move
            print("Player 1, your turn")
            position = player_input(valid_moves)
            
            # Place current player's marker on the board, remove a valid move...
            # Return the values for the new board and valid_moves
            board,valid_moves = place_marker(board, valid_moves, marker, position)
            display_board(board)
            won,message = check_won(board)
            if won:
                print('Congratulations, Player 1 ' + message)
                game_on = False
            
        else:
            # player2's turn
            # marker set for player2
            marker = player2
            
            # the player picks his move
            print("Player 2, your turn")
            position = player_input(valid_moves)
            
            # Place current player's marker on the board, remove a valid move...
            # Return the values for the new board and valid_moves
            board,valid_moves = place_marker(board, valid_moves, marker, position)
            display_board(board)
            won,message = check_won(board)
            if won:
                print('Congratulations, Player 2 ' + message)
                game_on = False
            
        
        # Change current player
        player1_turn = change_player(player1_turn)

        
        # Check for draw, and if so, break the while loop 
        if not won:
            game_on = full_board_check(valid_moves)
        
        
        
    keep_playing = replay()

# Final message
print("Thanks for playing!")
