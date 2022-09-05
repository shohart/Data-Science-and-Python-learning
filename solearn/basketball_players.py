"""First task from SoloLearn DS_Python course.
    Counts a number of basketball players who's height 
    is in the range of Standart deviation for a list.
 
    It is a bit tricky to do without usage 
    of statistics or numpy modules.
"""

players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]

pmean = sum(players) / len(players)

std = 0.0
for p in players:
    std += (p - pmean) ** 2

std = round((std / len(players)) ** (1/2), 2)
p_max = round((pmean + std), 2)
p_min = pmean - std

count = 0
for p in players:
    if p >= p_min and p <= p_max:
        count += 1
        
print (count)