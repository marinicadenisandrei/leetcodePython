# Leetcode - 268. Missing Number (Python laguage) - Easy

from termcolor import colored

print(colored("Leetcode - 268. Missing Number (Python laguage) -","yellow"), colored("Easy","green"))

def missingNumber(numsVar):
    numsVar.sort()

    for i in range(len(numsVar) - 1):
        if numsVar[i + 1] - numsVar[i] > 1:
            return numsVar[i] + 1
    
    return numsVar[-1] + 1

nums = [[3,0,1], [0,1], [9,6,4,2,3,5,7,0,1]]

for test in range(len(nums)):
    print(colored(f"Test {(test + 1)}:","green"), missingNumber(nums[test]), "|", colored("Passed", "green"))