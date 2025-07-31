# Leetcode - 327. Count of Range Sum (Python language) - Hard

from termcolor import colored

print(colored("Leetcode - 327. Count of Range Sum (Python language) -","yellow"), colored("Hard","red"))

def CountRangeSum(numsVar, lowerVar, upperVar):
    result = 0

    for i in range(len(numsVar)):
        for j in range(len(numsVar) + 1):
            if sum(numsVar[i:j]) >= lowerVar and sum(numsVar[i:j]) <= upperVar and len(numsVar[i:j]) > 0:
                result += 1
    
    return result
    
nums = [[-2,5,-1],[0]]
lower = [-2,0]
upper = [2,0]

for test in range(len(nums)):
    print(colored(f"Test {(test + 1)}:","green"), CountRangeSum(nums[test], lower[test], upper[test]), "|", colored("Passed","green"))
    