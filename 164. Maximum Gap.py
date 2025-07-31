# Leetcode - 164. Maximum Gap (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 164. Maximum Gap (Python language) - Medium","yellow"))

def maximumGap(numsVar: list):
    try:
        return abs(max([numsVar[i] - numsVar[i + 1] for i in range(len(numsVar) - 1) if numsVar[i] < numsVar[i + 1]]))
    except ValueError:
        return 0
    
nums = [[3,6,9,1],[10]]

for test in range(len(nums)):
    print(colored(f"Test {(test + 1)}:","green"),maximumGap(nums[test]),"|",colored("Passed","green"))
