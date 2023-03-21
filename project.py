
import csv
from colorama import Fore, Style
import urllib.request
import random



LENGTH = 5 #Global variable: word length
NUM_ATTEMPTS = 6 #Global variable: number of allowed attempts


#Setting up word bank
word_url = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
req = urllib.request.Request(word_url, headers=headers)
response = response = urllib.request.urlopen(req)
long_txt = response.read().decode()
words = long_txt.splitlines()
final_word_list = [word for word in words if len(word)==LENGTH and word.islower()]


def main():

    #Defining game rules to user
    print(
        "\n\n\n***Welcome to Wordle-ish: a fake wordle game*** \n\n"
        "Rules:\n\n"
        f"-You have {NUM_ATTEMPTS} attempts to guess a randomly generated word\n"
        "-After every attempt, the letters will change colors to indicate their positioning as follows:\n"
        "   *Green: this letter is in the correct position\n"
        "   *Yellow: This letter exists but is not in the correct position\n"
        "   *No color: This letter does not exist \n"
        f"-All word are {LENGTH} characters long\n"
        "-Words can't be plural (unless they dont end with s)\n"
        "-You will now be prompted for your first attempt\n\n"
        "GOOD LUCK\n\n"

    )


    #Setting up highscore streak
    current_score = 0
    with open("highscores.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            high_score = int(row[0])


    play_again = True
    while play_again == True: #Infinite loop, user prompted to exit after each game

        wordle = random.choice(final_word_list)

        for attempt in range(NUM_ATTEMPTS):

            #Gets a valid input from the user and retrieves results (Green/yellow)
            print (f"attempt #{attempt+1}: ", end="")
            word = get_valid_input().lower()
            results = check_word(word, wordle)

            #Prints results as colored text
            for i in range(LENGTH):
                print (colored_word(results, word)[i], end="")
                print(Style.RESET_ALL, end="")
            print ("")

            #Exits loop if correct word is reached. Increments score
            if word == wordle:
                print (Fore.GREEN + f"\nCORRECT WOOO, That took you {attempt+1} attempts!")
                print(Style.RESET_ALL)
                current_score+=1
                break

        #Reststs streak and annownces correct word if user fails
        if word != wordle:
            current_score = 0
            print (Fore.RED + "\nOOPS, GAMEOVER!!\n"
            f"The correct word was {wordle.upper()}")

        print(Style.RESET_ALL)


        #Checks if new highscore is achived and stores it in CSV file

        if current_score>high_score:
            high_score = current_score
            with open("highscores.csv", "w") as file:
                writer = csv.writer(file)
                writer.writerow([current_score])

        #prints current score and highscore
        print (
                    f"Current streak: {current_score}\n"
                    f"Highscore: {high_score}\n"
                    )

        #Prompts user to play again (retains current and high score) or exit (only retains highscore)
        if input("Would you like to play again? Y/N ").strip().lower() != "y":
            play_again = False
        print("\n\n")





def check_word(word, wordle):
    letters_result = []
    wordle_copy = wordle
    for i in range(len(word)):
        if word[i] == wordle[i]:
            letters_result.append("G")
            wordle_copy = wordle_copy.replace(word[i], '', 1)
        elif word[i] in wordle_copy:
            if word.count(word[i]) > wordle.count(word[i]):
                wordle_copy = wordle_copy.replace(word[i], '', 1)
            letters_result.append("Y")
        else:
            letters_result.append("N")
    return letters_result


def colored_word(results, word): #Colors the letters of the word based on their results
    color_codes = []
    for i in range(len(word)):
        if results[i] == "G":
            color_codes.append(Fore.GREEN + word[i])
        if results[i] == "Y":
            color_codes.append(Fore.YELLOW + word[i])
        if results[i] == "N":
            color_codes.append(word[i])
    return color_codes


def get_valid_input(): #Prompts user for input until a valid (real+correct length) word is entered
    while True:
        word = input().strip()
        if not check_length(word):
            print("Incorrect length, please try again")
        elif not check_real_word(word):
            print("Not in word bank, please try again")
        else:
            return word

def check_real_word(word, list=final_word_list): #Checks if word is in the word list
    return word in list
def check_length(word, length=LENGTH): #Checks if word is correct length
    return len(word) == length


if __name__ == "__main__":
    main()