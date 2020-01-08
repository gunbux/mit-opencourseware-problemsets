# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()
# your code begins here!

def hangman():
# define winconiditions and lose conditions and other variables

    word = choose_word(wordlist)
    lives = 8
    winCondition = 0
    onScreenDisplay = ''
    letters = 'abcdefghijklmnopqrstuvwxyz'
    guess = ''
    print word

    for i in range(0,len(word)):

        onScreenDisplay += '_ '
    
    
#print starting messages
    print 'Welcome to the game, Hangman!'
    print 'I am guessing of a word that is ', len(word) , ' letters long' 

#interactive guessing portion
    while winCondition == 0 and lives != 0:

        print 'You have ' , lives , ' guesses left'
        print 'Available letters: ' , letters

        guess = str(raw_input('Please guess a letter: ')).lower()

        if letters.find(guess) == -1:
            print 'The letter has already been used'

        elif word.find(guess) == -1:
            lives -= 1
            print 'Oops! That letter is not in my word: ' , onScreenDisplay

        else:
            for i in range(0,len(word)):

                if word[i] == guess:
                    n = i*2
                    onScreenDisplay = onScreenDisplay[0:n] + guess + onScreenDisplay[n+1:]

            print 'Good guess: ' , onScreenDisplay

        letters = letters.replace(guess, '')
        
        if onScreenDisplay.find('_') == -1:
             winCondition = 1

    if winCondition == 1:

        print 'Congratulations you won!'

    elif lives == 0:

        print 'You ran out of lives!'
        print 'The word was' , word
            
