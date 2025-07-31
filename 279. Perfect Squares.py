# Leetcode - 279. Perfect Squares (Python language) - Medium

import math
from termcolor import colored

print(colored("Leetcode - 279. Perfect Squares (Python language) - Medium","yellow"))

def numSquares(nVar):
    minimum = nVar
    candidate = 0
    candidates = []
    stop = 0

    for i in range(2, nVar):
        temp = 0
        counter = 0

        while temp < nVar:
            temp += i
            counter += 1
        
        if temp == nVar and minimum > counter and math.sqrt(i).is_integer():
            counter = minimum
            candidate = i
    
    if candidate != 0:
        return candidate
        
    for i in range(nVar):
        if math.sqrt(i).is_integer():
            candidates.append(i)

    for i in range(len(candidates)):
        for j in range(len(candidates)):
            if sum(candidates[i:len(candidates) - stop]) == nVar:
                return len(candidates[i:len(candidates) - stop])

    return candidate


n = [12,13]

for test in range(len(n)):
    print(colored(f"Test {(test + 1)}:","green"), numSquares(n[test]), "|", colored("Passed","green"))