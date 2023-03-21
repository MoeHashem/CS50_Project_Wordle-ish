#Wordle-ish: A simplified Wordle game

###Video Demo: https://youtu.be/GrDzmxv6QHE

###Description:

This is a python script that implements a word guessing game. The game is called "Wordle-ish" and is a simplified version of the popular game "Wordle". The unique element os the script is the utilization the colorama library to display colored text to indicate the correctness of the user's guesses.

The game follows closely to thwe original Wordle game as follows:

The game randomly chooses a word from a pre-defined list of words, which are all five letters long, and the user is given six attempts to guess the word. After every attempt, the letters of the user's guess will change color to indicate their positioning in the target word as follows:

Green: the letter is in the correct position
Yellow: the letter exists but is not in the correct position
No color: the letter does not exist in the target word

If the user correctly guesses the word, their score is incremented and they are prompted to play again. If they fail to guess the word, their score is reset to zero and they are also prompted to play again. The script also keeps track of the user's highest score, which is stored in a CSV file. The game is implemented using Python's built-in libraries, such as csv, urllib, and colorama.



To run the script, simply open a terminal, navigate to the directory where the script is located, and run python project.py.

The script is divided into several functions, including main(), get_valid_input(), check_word(), and colored_word().

The main() function sets up the game rules and the highscore tracking. It also runs multiple loops to allow the user to seamlessly input their attempts. The main() function calls on other functions to recieve, process, and validate user inputs

The check_word() function does the bulk of the checking where it iteratively checks each letter in the user input against the correct solution and assigns it a correct/incorrect indicator.
The most difficult part of this function was to check for duplicate letters and make sure they are all labelled correctly as per the original Wordle rules.

The check_real_word() and check_length() functions are just simple functions to ensure that the user input is the correct length and is a valid word according to the pre-defined list of words.

The get_valid_input() function starts an infinite loop and prompts the user for a valid input using the functions mentioned above.

The colored_word() function colors the letters according to thir indicator (from the check_word() function) using the colorama library.

The user highscore is stored in a CSV file names highscores.csv
This file only contains the highscore and the main script automatically increments the highscore if the user wins more than the current highscore games in a row.
To reset the highscore, the user must manually open the csv file and set the score to 0

The test_project file contains unit tests for all the mentioned functions.
