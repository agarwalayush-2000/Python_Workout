# Number guessing game

from random import randint, choice


def guessing_game():
    
    actual_number = randint(0, 100)
    actual_base = randint(2, 16)
    
    print(f'Number base in which you have to make a guess: {actual_base}')
    
    no_of_guesses = 7
    
    while no_of_guesses:
        # print(actual_number)
        
        guessed_number = int(input(f'Guess your number in {no_of_guesses} attempts: '), actual_base)
        
        if guessed_number == actual_number:
            print('You guessed the right number.')
            break
        
        if guessed_number < actual_number:
            print('Oops!! You guessed the lower number. Try again...')
            
        if guessed_number > actual_number:
            print('Oops!! You guessed the higher number. Try again...')

        no_of_guesses -= 1

    else:
        print('You lost the game!!')
        return

    print('Congrats!! You won this game.')


guessing_game()


DICTIONARY = ['at', 'of', 'am', 'say', 'all']


def guess_the_word(dictionary):

    actual_word = choice(dictionary).lower()

    while True:
        word = input('Guess the word from dictionary:')
        if word == actual_word:
            print('Congrats!! You won the game. Where is the party?')
            break

        elif word < actual_word:
            print('Oops!! You guessed the earlier word. Please think beyond the word.')

        elif word > actual_word:
            print('Oops!! You guessed the farther word. Please think under the word.')


guess_the_word(DICTIONARY)
