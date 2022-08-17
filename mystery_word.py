import random


wrong_letters = []
right_letters = []

with open('test-word.txt', 'r') as reader:
# read the file that is passed in
    contents = reader.read()
# create a list of the words
    word_list = contents.split()
#choose a random word in the list
    magic_word = random.choice(word_list)
    print(magic_word)
    # create a list of letters of magic_word
    magic_list = list(magic_word)
    print(magic_list)

remaining_guesses = 8

def play_game(magic_list):
        print(f"The magic word is {len(magic_list)} letters long.")
        print_board(magic_list, right_letters)
        guess_word(magic_list, remaining_guesses, wrong_letters, right_letters)

    # for letter of letter in letters, if input == letter, print CORRECT and display the letter

underscore = "_  "

def guess_word(magic_list, remaining_guesses, wrong_letters, right_letters):
    """"""
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
                    print(f"The magic word was {magic_word}! Better luck next time.")

        else:  
            print("Correct! Keep it up") 
            # loop through the letters in magic_list
            if guess in right_letters:
                print("HOWEVER you already guessed that, silly goose! Try again.")
                print(f"{board}\n")
                guess_word(magic_list, remaining_guesses, wrong_letters, right_letters)
            else:
                for i in range(len(magic_list)):
                    if guess == magic_list[i]:
                        right_letters.append(guess)
                        board = print_board(magic_list, right_letters)
                        print(f"{board}\n")
                        print(f"You have {remaining_guesses} guesses left\n")
                if "_" not in board:
                    print("You won! Good job")
                    return 



def print_board(magic_word, right_letters):
    """Print right letters and empty spaces
    
        This function takes two variables, the word to be guessed and the list of correct 
        letters guessed and returns a display of the correct letters and underscores for the remaining letters"""
    output = ""
    for letter in magic_word:
        if letter in right_letters:
            output += letter
        else:
            output += "_ "
    # print(output)
    return(output)


#do not touch
if __name__ == "__main__":
    play_game(magic_word)
