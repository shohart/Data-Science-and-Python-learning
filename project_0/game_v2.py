"""Game to guess a number. Shows you number of tries used.
Your pc gueses a number that you picked by itself!
"""
import numpy as np


def random_predict(number: int = 1) -> int:
    """Function to try guess a number using random method.

    Args:
        number (int, optional): Guessed number. Defaults to 1.

    Returns:
        int: number of tries needed
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1,101) # guessed number
        if number == predict_number:
            break
    return(count)


def score_game(random_predict) -> int:
    """Score prediction method

    Args:
        random_predict (_type_): prediction function

    Returns:
        int: number of mean tries
    """
    count_ls =[]
    np.random.seed(1) # fix the seed
    random_array = np.random.randint(1, 101, size=(1000)) # Create a list of numbers to guess
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f'Your function used {score} tries!')
    return(score)

if __name__ == '__main__':
    #RUN
    score_game(random_predict)

# print(f'Number of tries: {random_predict(90)}')