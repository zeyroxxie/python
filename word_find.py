# Name:  
# Student Number:  

# This file is provided to you as a starting point for the "word_find.py" program of Assignment 2
# of Programming Principles in Semester 2, 2026.  It aims to give you just enough code to help ensure
# that your program is well structured.  Please use this file as the basis for your assignment work.
# You are not required to reference it.

# The "pass" command tells Python to do nothing.  It is simply a placeholder to ensure that the starter files run smoothly.
# They are not needed in your completed program.  Replace them with your own code as you complete the assignment.


# Import the necessary modules.
import enchant # Used to send a request to the Pyenchant.
import json # Used to convert between JSON-formatted text and Python variables.
import string # Used to provide convenient access to a string variable containing all uppercase letters.
import random # Used to randomly select letters.



# This function generates and returns a list of 9 letters.  It has been completed for you.
# See Point 1 of the "Functions in word_find.py" section of the assignment brief.
def select_letters():
    # This tuple contains 26 numbers, representing the frequency of each letter of the alphabet in Scrabble.
    letter_weights = (9, 2, 2, 4, 12, 2, 3, 2, 9, 1, 1, 4, 2, 6, 8, 2, 1, 6, 4, 6, 4, 2, 2, 1, 2, 1)

    # The letter_weights tuple is used in this call to the "random.choices()" function, along with
    # the pre-defined "string.ascii_uppercase" variable which contains the letters A to Z.
    chosen_letters = random.choices(string.ascii_uppercase, weights=letter_weights, k=9)

    # We've selected a list of 9 random letters using the specified letter frequencies, and now return it.
    return chosen_letters



def display_letters(letters): 
    pass

    

def validate_word(word, letters):
    pass


