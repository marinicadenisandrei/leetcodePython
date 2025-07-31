# Leetcode - 258. Add Digits (Python language) - Easy

from termcolor import colored

print(colored("Leetcode - 258. Add Digits (Python language) -", "yellow"), colored("Easy","green"))

def addDigits(numVar):
    while len(str(numVar)) > 1:
        sumVar = 0

        for i in str(numVar):
            sumVar += int(i)
        
        numVar = sumVar
    
    return numVar
            

num = [38,0]

for test in range(len(num)):
    print(colored(f"Test {(test + 1)}:","green"), addDigits(num[test]), "|", colored("Passed","green"))