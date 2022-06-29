"""
File: word_guess.py
-------------------
Fill in this comment.
"""


import random


LEXICON_FILE = "Lexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8             # Initial number of guesses player starts with


def play_game(secret_word):
    """
    Add your code (remember to delete the "pass" below)
    """
    guess_word = [] # create an empty list to check wheather the give character is in the secret word 
    for letter in secret_word:
        guess_word.append(letter)

    word_dash = []  #create an empty list of dashes for the count of characters in a secret word
    for letter in secret_word:
        word_dash.extend('_')
    
    lost_attempts = 0  #'0' is used to set the count of failed attempts
    attempts_left = INITIAL_GUESSES #the number of attempts the user still have
    print("The word now looks like this: "+str(word_dash))
    print("You have "+str(INITIAL_GUESSES)+" guesses left")

    while lost_attempts < INITIAL_GUESSES:   #keep asking the user for guess until the condition is true
        char_count = 0

        get_letter = input("Type a single letter here, then press enter: ")
        get_letter = get_letter.upper() #converting the user from lower case to upper case
        if len(get_letter) > 1 :  #user should enter a single character once at a time 
            print("Guess should only be a single character.")

        if get_letter in guess_word:  #update the user if entered letter is in the secret world--
            print("That guess is correct.")
            char_count = guess_word.count(get_letter)
            temp = guess_word.index(get_letter)
            word_dash[temp] = get_letter   #filled the dash list with correctly guessed letter
            for i in range(char_count - 1):
                temp = guess_word.index(get_letter,temp + 1)
                word_dash[temp] = get_letter
            if '_' not in word_dash:     #check the all the dashes are filled with message we entered
                print("Congratulations, the word is: "+str(secret_word))
                break
            print("The word now looks like this: " +str(word_dash))
            print("You have " + str(attempts_left)+ " guesses left")

        else:
            lost_attempts = lost_attempts + 1     #if the guess is wrong increment the losted attempts
            attempts_left = INITIAL_GUESSES - lost_attempts
            if lost_attempts == INITIAL_GUESSES:    #check if the losted attempts is equal to the constant value
                print("There are no "+str(get_letter)+"'s in the word")
                print("Sorry, you lost. The secret word was:" +str(secret_word))
            else:     #check if condition given is false display the word 
                print("There are no "+str(get_letter)+"'s in the word")
                print("The word now looks like this: "+str(word_dash))
                print("You have "+str(attempts_left)+" guesses left")


def get_word():
    """
    This function returns a secret word that the player is trying
    to guess in the game.  This function initially has a very small
    list of words that it can select from to make it easier for you
    to write and debug the main game playing program.  In Part II of
    writing this program, you will re-implement this function to
    select a word from a much larger list by reading a list of words
    from the file specified by the constant LEXICON_FILE.
    """
    """index = random.randrange(3)
    if index == 0:
        return 'HAPPY'
    elif index == 1:
        return 'PYTHON'
    else:
        return 'COMPUTER'
        """

    filename = open(LEXICON_FILE, "r")   #opening the file
    word_list = [] #empty is to store words in the lexicon file
    for word in filename:
        word_list.append(word.strip())   #read the each line in the file then append the list
    secret_word = random.choice(word_list)   #choose the word randomly
    return secret_word

def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    secret_word = get_word()
    play_game(secret_word)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
