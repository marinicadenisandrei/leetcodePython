# Leetcode - 167. Two Sum II - Input Array Is Sorted (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 167. Two Sum II - Input Array Is Sorted (Python language) - Medium","yellow"))

def twoSum(numbersVar: list, targetVar: int):
    i = 0
    j = len(numbersVar) - 1

    while i < j:
        if numbersVar[i] + numbersVar[j] == targetVar:
            return [i+1,j+1]
            
        elif (numbersVar[i] + numbersVar[j] > targetVar):
            j -= 1
        else:
            i += 1
    
numbers = [[2,7,11,15],[2,3,4],[-1,0]]
target = [9,6,-1]

for test in range(len(target)):
    print(colored(f"Test {(test + 1)}:","green"),twoSum(numbers[test], target[test]),"|",colored("Passed","green"))