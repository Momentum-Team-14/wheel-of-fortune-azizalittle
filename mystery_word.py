import random

wrong_letters = []
right_letters = []
magic_word = ''
remaining_guesses = 8
underscore = "_  "

def print_board(magic_word, right_letters):
    """Print right letters and empty spaces
    
        This function takes two variables, the word to be guessed and the list of correct 
        letters guessed and returns a display of the correct letters and underscores for the remaining letters"""
    output = ""
    # loops through list of magic_word's letters
    for letter in magic_word:
        if letter in right_letters:
            # displays right letter in it's respective place
            output += letter
        else:
            # displays underscore in it's respective place
            output += "_ "
    return(output)


def guess_word(magic_list, remaining_guesses, wrong_letters, right_letters):
    """Guess the letters
    
        This function takes four paramters, the list of letters in magic_word, the number of
        guesses remaining, the list of wrong letters guessed and the list of correct letters
        guessed. It loops through the letters in magic word, and if the user guesses any letter correctly, it will notify them, update the board and update the number of guesses remaining. If the user makes a repeated guess, they will be notifies and number of guesses will not change. If the user guesses incorrectly, the wrong letter will be displayed and number of guesses will decrease by one. As long as there are guesses left and empty spaces in the board, they will be prompted to guess again after each round. """
    # start with emptpy guesses for each time the game is played
    right_letters = []
    wrong_letters = []
    # loop through 8 rounds of guessing
    while remaining_guesses > 0:
        # ask user to guess a letter
        guess = input('Guess a letter in the magic word! ')
        if guess not in magic_list:
            # if user repeated an incorrect guess
            if guess in wrong_letters:
                    remaining_guesses += 0
                    print("You already guessed that, silly goose! Try again.")
                    # display number of guesses remaining
                    print(f"You have {remaining_guesses} guesses left\n")
                    # prompt to guess again
                    guess_word(magic_list, remaining_guesses, wrong_letters, right_letters)
            else:       
                # add incorrect guess to wrong_letters, 
                wrong_letters.append(guess)
                # subtract 1 from number of guesses remaining
                remaining_guesses -= 1
                # display wrong guesses
                print(f"Incorrect: {''.join(wrong_letters)}")
                board = print_board(magic_list, right_letters)
                # display board with right letters
                print(board)
                print(f"You have {remaining_guesses} guesses left\n")
                # end game if they run out of guesses
                if remaining_guesses == 0:
                    print("You ran out of guesses, womp womp!")
                # tell user the magic word
                    print(f"The magic word was {''.join(magic_list)}! Better luck next time.")

        else:  
            print("Correct! Keep it up") 
            # loop through the letters in magic_list
            if guess in right_letters:
                # if user makes a repeated correct guess
                print("HOWEVER you already guessed that, silly goose! Try again.")
                # print board
                print(f"{board}\n")
                # prompt to guess again
                guess_word(magic_list, remaining_guesses, wrong_letters, right_letters)
            else:
                for i in range(len(magic_list)):
                    # if user makes a new correct guess
                    if guess == magic_list[i]:
                        # add guess to list of right words
                        right_letters.append(guess)
                        board = print_board(magic_list, right_letters)
                        # print board
                        print(f"{board}\n")
                        #display number of guesses left
                        print(f"You have {remaining_guesses} guesses left\n")
                if "_" not in board:
                # if user guesses magic_word, end the game
                    print("You won! Good job")
                    break
    # ask user if they want to play again
    play_again = input("Do you want to play again? yes or no: ")
    if play_again == 'yes':
        choose_level(word_list)


def play_game(magic_list):
    """Play actual guessing game
    
        This function takes one parameter, the list of letters in magic_word and starts the guessing game with the required arguments"""
    # Give the user a hint of magic_word's length
    print(f"The magic word is {len(magic_list)} letters long.")
    guess_word(magic_list, remaining_guesses, wrong_letters, right_letters)


def choose_level(word_list):
    """Selects word for respective level
    
        This function takes one parameter, the list of words and filters through each word based on the length. It splits the words into 3 groups, and chooses one based on the user input for level of difficulty. Then starts the game with selected word"""
    easy_words = [word for word in word_list if len(word) <= 6]
    normal_words = [word for word in word_list if 6 >= len(word) <= 8]
    hard_words = [word for word in word_list if len(word) > 8]
    # prompt user for level of difficulty
    level = input('Choose a level of difficulty: easy, normal or hard: ')
    if level == 'easy':
        magic_word = random.choice(easy_words)
    elif level == 'normal':
        magic_word = random.choice(normal_words)
    else:
        magic_word = random.choice(hard_words)
    # create a list of letters of magic_word
    magic_list = list(magic_word)
    play_game(magic_list)

with open('words.txt', 'r') as reader:
# read the file that is passed in
    contents = reader.read()
# create a list of the words
    word_list = contents.split()
# establishes level of difficulty before the game begins
    choose_level(word_list)


#do not touch
if __name__ == "__main__":
    play_game(magic_word)
