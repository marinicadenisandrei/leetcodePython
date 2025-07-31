# Leetcode - 154. Find Minimum in Rotated Sorted Array II (Python language) - Hard

from termcolor import colored

print(colored("Leetcode - 154. Find Minimum in Rotated Sorted Array II (Python language) -", "yellow"), colored("Hard", "red"))

def findMin(numsVar : list):
    return min(numsVar)

nums = [[1,3,5],[2,2,2,0,1]]

for test in range(len(nums)):
    print(colored(f"Test {(test + 1)}:", "green"),findMin(nums[test]), "|", colored("Passed", "green"))