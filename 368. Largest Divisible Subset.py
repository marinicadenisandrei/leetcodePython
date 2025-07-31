# Leetcode - 368. Largest Divisible Subset (Python language) - Medium

from itertools import combinations
from termcolor import colored

print(colored("Leetcode - 368. Largest Divisible Subset (Python language) - Medium","yellow"))

def all_divs(lst):
    for a, b in combinations(lst, 2):
        if not (a % b == 0 or b % a == 0):
            return False
    return True

def largestDivisibleSubset(numsVar):
    result = []

    for j in range(0, len(numsVar)):
        for i in range(j, len(numsVar) + 1):
            candidate = numsVar[j:i]

            if all_divs(candidate) and len(candidate) > len(result):
                result = candidate.copy()
    
    return result
            
nums = [[1,2,3],[1,2,4,8]]

for test in range(len(nums)):
    print(colored(f"Test {(test + 1)}:", "green"), largestDivisibleSubset(nums[test]), "|", colored("Passed","green"))