from collections import deque, OrderedDict
import numpy as np

def brackets(line):
    dq = deque()
    for x in line:
        if x == '(':
            dq.append(x)
        elif x == ')':
            try:
                dq.pop()
            except IndexError:
                return False
    if len(dq) == 0:
        return True
    else:
        return False
        
        
print(np.iinfo(np.int64))
print(*sorted(map(str, set(np.sctypeDict.values()))), sep='\n')

print(np.uint8(-456))

arr, step = np.linspace(-6, 21, 60, endpoint=False, retstep=True)
print(round(step, 2))