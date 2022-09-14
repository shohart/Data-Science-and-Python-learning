from statistics import mean
import numpy as np
import statistics as st

def get_unique_loto(num):
    fullfield = np.zeros((num,5,5))
    
    for n in range(num):
        field = np.random.choice(range(0, 101), size=(5, 5), replace=False)
        fullfield[n] = field

    return fullfield

print(get_unique_loto(7))