"""Game to guess a number. Shows you number of tries used.
"""
import numpy as np

number = np.random.randint(1, 101) # Generate a number
count = 0 # number of tries
while True:
    count += 1
    pridoct_number = int(input("Guess a number, from 1 to 100:\n"))
    
    if pridoct_number > number:
        print('Number should be less!')
    elif pridoct_number < number:
        print('Number should be more!')
    else:
        print(f"You found a number! It is {number}, you used {count} tries!")
        break # Game over
