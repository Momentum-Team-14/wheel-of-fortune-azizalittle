import random


remaining_guesses = 0
wrong_letters = []
right_letters = []

def play_game():
    # read the file that is passed in
    with open('test-word.txt', 'r') as reader:
        contents = reader.read()
    # create a list of the words
        word_list = contents.split()
    #choose a random word in the list
        magic_word = random.choice(word_list)
        print(magic_word)
        magic_length = len(magic_word)
    # create a list of letters of magic_word
        letters = list(magic_word)
        print(letters)
        print(magic_length)
        print(f"The magic word is {magic_length} letters long.")
        print_board(magic_word)
        guess_word(magic_word, remaining_guesses, wrong_letters, right_letters)

    # for letter of letter in letters, if input == letter, print CORRECT and display the letter


def guess_word(magic_word, remaining_guesses, wrong_letters, right_letters):
    """"""
    # ask user to guess a letter
    guess = input('Guess a letter in the magic word! ')
    # loop through 8 rounds of guessing
    # HOW THE HELL DO YOU LOOP IN PYTHON WITHOUT EMBEDDING IT
    while remaining_guesses < 9:
        if guess not in magic_word:
            print("incorrect")
            # add guessed letter to list of wrong words
            wrong_letters.append(guess)
            # update remaining guesses
            remaining_guesses += 1
            # display wrong guesses
            print(wrong_letters)
            print(f"You have {remaining_guesses} guesses left")
        else:  
            print("correct!") 
            # add guessed letter to list of right words
            right_letters.append(guess)
            # update remaining guesses
            remaining_guesses += 1
            print(f"You have {remaining_guesses} guesses left")
        print_board(magic_word, right_letters)
        play_game(magic_word)
    print("You ran out of guesses, womp womp!")



def print_board(magic_word, right_letters):
    """Print right letters and empty spaces
    
        This function takes two variables, the word to be guessed and the list of correct 
        letters guessed and returns a display of the correct letters and underscores for the remaining letters"""
    underscore = "_  "
    output = ""
    for letter in magic_word:
        if letter in right_letters:
            output += letter
        else:
            output += "_ "
    print(output)

#do not touch
if __name__ == "__main__":
    play_game()
