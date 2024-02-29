# Assigment 2 - Hangman Game Variation
# Author: Dania Tamayo-Vera
# Collaborators: Chris Vessey, Gurjit Randhawa

# Utility functions
# You do not need to understand the implementation of these utilities functions
# but you need to know how to use these functions

from random import choice
from typing import List

WORD_LIST = 'game_words.txt'


def get_list_of_words():
    """
    This function reads the .txt file and returns a list with
    all the words contained in this file
    :return List of words
    """

    print("Loading list of words from file....")

    with open(WORD_LIST, 'r') as f:
        line = f.readline()
        list_of_words = line.split()

    print(f"{len(list_of_words)} words were loaded.")
    return list_of_words


def select_random_word(words_list: List):
    """
    This function takes as a parameter a list of words and
    returns one word chosen randomly
    :param words_list: list of words
    :return string
    """
    return choice(words_list)



def guessed_word(computer_word: str,
                 user_guessed_letters: List[str]):
    # Pass your code here - This is the same function you implemented in Problem 1
    # You MUST delete "pass"
    pass


def letters_available(user_guesses: List[str]):
    # Pass your code here - This is the same function you implemented in Problem 1
    # You MUST delete "pass"
    pass

def guessed_word(computer_word: str,
                 user_guessed_letters: List[str]):
    # Write your code here
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
    # Write your code here
    count = -1
    letters_remaining = "abcdefghijklmnopqrstuvwxyz"
    for q in user_guesses:
        for z in letters_remaining:
            count = count + 1
            if q == z:
                letters_remaining = letters_remaining[0: count] + letters_remaining[count + 1:]
        count = -1
    return letters_remaining.lower()