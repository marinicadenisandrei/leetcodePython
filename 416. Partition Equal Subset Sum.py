# Leetcode - 416. Partition Equal Subset Sum (Python language) - Medium 

from itertools import permutations
from termcolor import colored

print(colored("Leetcode - 416. Partition Equal Subset Sum (Python language) - Medium", "yellow"))

def canPartition(numsVar):
    for c in permutations(nums, len(numsVar)):
        for i in range(len(c) - 1):
            c = list(c)
            if sum(c[:i + 1]) == sum(c[i + 1:]):
                return True
    
    return False

nums = [[1,5,11,5],[1,2,3,5]]

for test in range(len(nums)):
    print(
        colored(f"Test {(test + 1)}:", "green"),
        canPartition(nums[test]),
        "|",
        colored("Passed", "green")
    )