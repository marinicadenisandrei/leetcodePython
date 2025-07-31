# Leetcode - 136. Single Number (Python language) - Easy

from termcolor import colored

print(colored("Leetcode - 136. Single Number (Python language) -", "yellow"), colored("Easy", "green"))

def singleNumber(numsVar : list):
    for i in range(len(numsVar)):
        temp = numsVar.copy()
        temp.pop(i)

        if numsVar[i] not in temp:
            return numsVar[i]

nums = [[2,2,1], [4,1,2,1,2], [1]]
    
for test in range(len(nums)):
    print(colored(f"Test {(test + 1)}:", "green"), singleNumber(nums[test]), "|", colored("Passed", "green"))



