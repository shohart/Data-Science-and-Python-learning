# Just a simple 'Guess where the ball' is game.
# Realized with three functions. First generates shuffled list with a template,
# second takes user input as a guess try,
# third matches guess with a shuffled list.


from random import shuffle


guess_list = [' ', 'O', ' ']


def shuffled_lst(lst):
    shuffle(lst)
    return lst


mixed_list = shuffled_lst(guess_list)


def player_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input('Pick a number to guess: 0, 1 or 2:\n')

    return int(guess)


guess = player_guess()


def check_guess(lst, guess):
    if lst[guess] == 'O':
        print(f'\nCorrect!\n{mixed_list}\n')
    else:
        print(f'\nWrong! Try again!\n{mixed_list}')


check_guess(mixed_list, guess)
