# Leetcode - 152. Maximum Product Subarray (Python language) - Medium

from functools import reduce
from termcolor import colored

print(colored("Leetcode - 152. Maximum Product Subarray (Python language) - Medium", "yellow"))

def maxProduct(numsVar : list):
    maxNumber = 0

    for i in range(1,len(numsVar) + 1):
        result = reduce(lambda x,y: x * y, numsVar[:i])
        if result > maxNumber: 
            maxNumber = result
    
    return maxNumber

nums = [[2,3,-2,4], [-2,0,-1]]

for test in range(len(nums)):
    print(colored(f"Test {(test + 1)}:", "green"), maxProduct(nums[test]), "|", colored("Passed", "green"))