# Name:
# Student Number:

# This file is provided to you as a starting point for the "word_find.py" program of Assignment 2
# of Programming Principles in Semester 2, 2026.  It aims to give you just enough code to help ensure
# that your program is well structured.  Please use this file as the basis for your assignment work.
# You are not required to reference it.


# Import the necessary modules.
import enchant # Used to send a request to the Pyenchant.
import json # Used to convert between JSON-formatted text and Python variables.
import string # Used to provide convenient access to a string variable containing all uppercase letters.
import random # Used to randomly select letters.


# Create the US English dictionary once, so that it can be used to check words throughout the game.
dictionary = enchant.Dict("en_US")

# The number of points each letter is worth in the game of Scrabble.
LETTER_POINTS = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1,
                 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1,
                 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10}



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



# This function prints the 9 letters in a 3x3 grid.
# See Point 2 of the "Functions in word_find.py" section of the assignment brief.
def display_letters(letters):
    print()
    print('               ' + letters[0] + ' | ' + letters[1] + ' | ' + letters[2])
    print('              -----------')
    print('               ' + letters[3] + ' | ' + letters[4] + ' | ' + letters[5])
    print('              -----------')
    print('               ' + letters[6] + ' | ' + letters[7] + ' | ' + letters[8])
    print()



# This function returns True if the word is made up only of the available letters, otherwise False.
# See Point 3 of the "Functions in word_find.py" section of the assignment brief.
def validate_word(word, letters):
    # Work on a copy of the letters so that the original list is not changed.
    remaining_letters = letters.copy()

    for character in word:
        if character in remaining_letters:
            # Remove the letter so that it cannot be used more times than it appears.
            remaining_letters.remove(character)
        else:
            return False

    return True



# This function returns True if the word is a recognised English word, otherwise False.
def is_english_word(word):
    # The word is checked in lowercase so that names (e.g. "Paris") are not accepted.
    return dictionary.check(word.lower())



# This function returns the Scrabble score of a word, by adding up the points of each letter.
def get_word_score(word):
    points = 0

    for character in word:
        points += LETTER_POINTS[character]

    return points



# Welcome the user and create the variables needed in the game (Requirement 1).
print('Welcome to Word Find.')
print('Come up with as many words as possible from the letters below!')

score = 0
used_words = []
letters = select_letters()


# Ask the user to select easy mode or hard mode, until they enter "E" or "H" (Requirement 2).
while True:
    print()
    mode = input('Do you wish to play [e]asy mode or [h]ard mode? ').upper()

    if mode == 'E':
        hard_mode = False
        print('Easy mode selected.  Entering an invalid word will not end the game.')
        break
    elif mode == 'H':
        hard_mode = True
        print('Hard mode selected.  Entering an invalid word will end the game!')
        break
    else:
        print('Invalid input, please select a mode.')


# The main game loop, which repeats until the game ends (Requirement 3).
while True:
    # Show the score and letters, then get the user's input (Requirement 3.1).
    print()
    print('Score: ' + str(score) + '.  Your letters are:')
    display_letters(letters)
    user_input = input('Enter a word, [s]huffle letters, [l]ist words, or [e]nd game): ').upper()
    print()

    # End the game (Requirement 3.2).
    if user_input == 'E':
        print('Ending game...')
        break

    # Shuffle the letters (Requirement 3.3).
    elif user_input == 'S':
        print('Shuffling letters...')
        random.shuffle(letters)

    # List the words entered so far (Requirement 3.4).
    elif user_input == 'L':
        if len(used_words) == 0:
            print('You have not yet entered any words.')
        else:
            used_words.sort()
            print('Previously entered words:')
            for word in used_words:
                print('  - ' + word)

    # The word is too short (Requirement 3.5).
    elif len(user_input) < 3:
        print('Word must be at least 3 letters long.', end='  ')
        if hard_mode:
            print('Game over!')
            break
        print()

    # The word has already been used (Requirement 3.6).
    elif user_input in used_words:
        print(user_input + ' has already been used.', end='  ')
        if hard_mode:
            print('Game over!')
            break
        print()

    # The word uses letters that are not available (Requirement 3.7).
    elif not validate_word(user_input, letters):
        print('Invalid character(s) used!', end='  ')
        if hard_mode:
            print('Game over!')
            break
        print()

    # Check that the word is a real English word, and award points if it is (Requirement 3.8).
    else:
        if is_english_word(user_input):
            points = get_word_score(user_input)
            score += points
            used_words.append(user_input)
            print(user_input + ' accepted - ' + str(points) + ' points awarded.  Your score is now ' + str(score) + '.')
        else:
            print(user_input + ' is not a recognised word.', end='  ')
            if hard_mode:
                print('Game over!')
                break
            print()


# Show the final score, and record a log of the game if the score is 50 or more (Requirement 4).
print()
print('Your final score was ' + str(score) + '.')

if score >= 50:
    print('Congratulations!  That is a great score - a log of this game has been saved.')

    # The letters and words are sorted alphabetically, as per the example in the assignment brief.
    log = {'letters': sorted(letters), 'words': sorted(used_words), 'score': score}

    # Load the existing logs.  If the file does not exist or is invalid, start with an empty list.
    try:
        file = open('logs.txt', 'r')
        logs = json.load(file)
        file.close()
    except Exception:
        logs = []

    # Add this game's log and write all of the logs back to the file.
    logs.append(log)
    file = open('logs.txt', 'w')
    json.dump(logs, file, indent=4)
    file.close()


# Thank the user (Requirement 5).
print('Thank you for playing!')
