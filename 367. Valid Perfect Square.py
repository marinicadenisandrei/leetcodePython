# Leetcode - 367. Valid Perfect Square (Python language) - Easy

import math
from termcolor import colored

print(colored("Leetcode - 367. Valid Perfect Square (Python language) -","yellow"), colored("Easy","green"))

def isPerfectSquare(numVar):
    return numVar == int(math.sqrt(numVar))**2 

num = [16,14]

for test in range(len(num)):
    print(colored(f"Test {(test + 1)}:", "green"), isPerfectSquare(num[test]), "|", colored("Passed","green"))
    