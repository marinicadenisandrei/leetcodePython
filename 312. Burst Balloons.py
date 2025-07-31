# Leetcode - 312. Burst Balloons (Python language) - Hard 

import math
from termcolor import colored

print(colored("Leetcode - 312. Burst Balloons (Python language) -", "yellow"), colored("Hard","red"))

def maxCoins(numsVar):
    index = 1
    result = 0

    while len(numsVar) > 2:
        result += (numsVar[index - 1] * numsVar[index] * numsVar[index + 1])
        numsVar.pop(1)


    while len(numsVar) > 0:
        result += math.prod(numsVar)
        numsVar.pop(0)


    
    return result
        
nums = [[3,1,5,8],[1,5]]

for test in range(len(nums)):
    print(colored(f"Test {(test + 1)}:","green"), maxCoins(nums[test]), "|", colored("Passed","green"))