# Assigment 2 Problem 2- Hangman Game Variation with Assiatnce
# Author: Dania Tamayo-Vera
# Collaborators: Chris Vessey, Gurjit Randhawa

from typing import List

from utils import get_list_of_words
from utils import select_random_word
from utils import guessed_word
from utils import letters_available
import random

# Getting the words from the word list provided
# This variable is defined in the scope of this program
# Thus it can be accessed from anywhere in the program

words = get_list_of_words()


def match_words(user_guessed_word: str,
                word_from_computer_list: str):
    #This code will return false if the length of word_from_computer is not the same as user_guessed_word
    if (len(user_guessed_word) != len(word_from_computer_list)):
        return False
    char_list = []
    #This code will take the letters in the user_guessed_word and put them in a list
    for i in range(len(user_guessed_word)):
        if (user_guessed_word[i] != "#"):
            char_list.append(i)
    #This code will return false if the letters in the user_guessed_word are not the same as word_from_computer
    for j in char_list:
        if (user_guessed_word[j] != word_from_computer_list[j]):
            return False
    return True


def get_possible_matches(user_word: str):
    list_word = []
    list_num = []
    count = -1
    #This code takes the index of the letters in user_word
    for char in user_word:
        count = count + 1
        if char != "#":
            list_num.append(count)
    # This code takes the words that has the same length as user_word
    for each_word in words:
        if len(each_word) == len(user_word):
            list_word.append(each_word)
    list_of_matches = []
    #This code takes the words that has the same index letters as the user_word index letters
    for new_word in list_word:
        count2 = 0
        for w in range(len(list_num)):
            if new_word[list_num[count2]] == user_word[list_num[count2]]:
                count2 = count2 + 1
            if new_word[list_num[count2 - 1]] != user_word[list_num[count2 - 1]]:
                count2 = 0
            if count2 == len(list_num):
                list_of_matches.append(new_word)
    print("This are the possible matches:")
    for matches_words in list_of_matches:
        print(matches_words)




def hangman_game_with_assistance(computer_word: str):
    user_guessed = []
    guesses = 6
    #Intro of hangman game
    print("Let’s play the Hangman game..")
    print(f"The computer has selected a word that is {len(computer_word)} letters long")
    print(f"You have {guesses} guesses")
    print(f"Your available letters are: {letters_available(user_guessed)}")
    # if the word isn't guessed yet and guesses != 0 will keep asking for input
    while guessed_word(computer_word, user_guessed) != computer_word and guesses != 0:
        user_guess = input("Input a letter: ")
        #This code will reduce the guesses remaining if the input isn't in the computer_word
        if user_guess not in computer_word or user_guess in user_guessed:
            #This code will not reduce guesses when the input is (*)
            if user_guess == "*":
                guesses = guesses
            else:
                user_guessed.append(user_guess)
                guesses = guesses - 1
                print(f"That is a wrong guess. You have {guesses} guesses lefts "
                    f"and your guessed word so far is {guessed_word(computer_word, user_guessed)}")
                print(f"You have {guesses} guesses")
                print(f"Your available letters are: {letters_available(user_guessed)}")
        #This code will say the guess is correct if the letter is in the computer_word
        if user_guess in computer_word:
            user_guessed.append(user_guess)
            print(f"That guess was right. Your guessed word is: {guessed_word(computer_word, user_guessed)}")
            print(f"You have {guesses} guesses")
            print(f"Your available letters are: {letters_available(user_guessed)}")
        #This code will give hint for the user and print the possible matches if he inputed (*)
        if user_guess == "*":
            get_possible_matches(guessed_word(computer_word, user_guessed))
            print(f"You have {guesses} guesses")
            print(f"Your available letters are: {letters_available(user_guessed)}")
        #This is the last part of the code which will print gratulationes if he won, if he lost it will print good luck
        if guessed_word(computer_word, user_guessed) == computer_word:
            return "Gratulationes, you have guessed the word!"
        if guesses == 0:
            return "Good luck, next time"


if __name__ == "__main__":
    hangman_game_with_assistance(select_random_word(words))

