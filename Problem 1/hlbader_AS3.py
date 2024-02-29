# Assigment 2 - Hangman Game Variation
# Author: Dania Tamayo-Vera
# Collaborators: Chris Vessey, Gurjit Randhawa
import random
# -----------------------------------

# Utility functions
# You do not need to understand the implementation of these utilities functions
# but you need to know how to use these functions

from random import choice
from typing import List

from utils import get_list_of_words
from utils import select_random_word

# Getting the words from the word list
# This variable is defined in the scope of this program
# Thus it can be accessed from anywhere in the program

words = get_list_of_words()


def guessed_word(computer_word: str,
                 user_guessed_letters: List[str]):
    #This code will replace the hashtags with letters if the letter is in computer_word
    unkown = "#"*len(computer_word)
    count = -1
    for a in user_guessed_letters:
        for i in computer_word:
            count = count + 1
            if a == i:
                unkown = unkown[0:count] + a + unkown[count+1:]
        count = -1
    return unkown


def letters_available(user_guesses: List[str]):
    #This code will return the letters that the user didn't use
    count = -1
    letters_remaining = "abcdefghijklmnopqrstuvwxyz"
    for q in user_guesses:
        for z in letters_remaining:
            #Count is an index counter
            count = count + 1
            if q == z:
                letters_remaining = letters_remaining[0: count] + letters_remaining[count + 1:]
        count = -1
    return letters_remaining.lower()



def hangman_game(computer_word: str):
    user_guessed = []
    guesses = 6
    # Intro of hangman game
    print("Let’s play the Hangman game..")
    print(f"The computer has selected a word that is {len(computer_word)} letters long")
    print(f"You have {guesses} guesses")
    print(f"Your available letters are: {letters_available(user_guessed)}")
    # if the word isn't guessed yet and guesses != 0 will keep asking for input
    while guessed_word(computer_word, user_guessed) != computer_word and guesses != 0:
        user_guess = input("Input a letter: ")
        # This code will reduce the guesses remaining if the input isn't in the computer_word
        if user_guess not in computer_word or user_guess in user_guessed:
            user_guessed.append(user_guess)
            guesses = guesses - 1
            print(f"That is a wrong guess. You have {guesses} guesses lefts and your guessed word so far is {guessed_word(computer_word, user_guessed)}")
            print(f"You have {guesses} guesses")
            print(f"Your available letters are: {letters_available(user_guessed)}")
        # This code will say the guess is correct if the letter is in the computer_word
        if user_guess in computer_word:
            user_guessed.append(user_guess)
            print(f"That guess was right. Your guessed word is: {guessed_word(computer_word, user_guessed)}")
            print(f"You have {guesses} guesses")
            print(f"Your available letters are: {letters_available(user_guessed)}")
        #This is the last part of the code which will print gratulationes if he won, if he lost it will print good luck
        if guessed_word(computer_word, user_guessed) == computer_word:
            return "Gratulationes, you have guessed the word!"
        if guesses == 0:
            return "Good luck, next time"




print(hangman_game(random.choice(words)))

if __name__ == "__main__":
    # Write your code here
    # You MUST delete "pass"
    pass
