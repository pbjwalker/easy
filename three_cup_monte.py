# three_cup_monte is a simple simulation of the cup and ball game.
# The 3 cups are simulated with a list.
# The random library shuffles the list.
# The player sees only a request for a guess and the answer.
# This is to help me learn more about functions.


# First we need to bring in the random library.
# Specifically, the shuffle() method.
from random import shuffle

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


def player_guess():
    guess = ''    
    while guess not in ['0','1','2']:     
        guess = input("Pick a number: 0, 1, or 2: ")
    return int(guess)  


def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print("Correct!")
        return False
    else:
        print("Nope! You missed it!")
        print(mylist)
        return True
        

# SETUP THE INITIAL LIST
mylist = ['','O','']
keep_playing = True

# PLAY GAME UNTIL YOU WIN
while keep_playing:
    # SHUFFLE THE LIST
    current_list = shuffle_list(mylist)
    
    # HAVE THE USER GUESS THE LOCATION
    made_a_guess = player_guess()
    
    
    # CHECK THE GUESS AGAINST THE LIST
    keep_playing = check_guess(current_list,made_a_guess)
