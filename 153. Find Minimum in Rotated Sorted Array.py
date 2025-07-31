# Leetcode - 153. Find Minimum in Rotated Sorted Array (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 153. Find Minimum in Rotated Sorted Array (Python language) - Medium", "yellow"))

def findMin(numsVar : list):
    return min(numsVar)

nums = [[3,4,5,1,2], [4,5,6,7,0,1,2], [11,13,15,17]]

for test in range(len(nums)):
    print(colored(f"Test {(test + 1)}:", "green"), findMin(nums[test]), "|", colored("Passed", "green"))