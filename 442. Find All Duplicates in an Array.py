# Leetcode - 442. Find All Duplicates in an Array (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 442. Find All Duplicates in an Array (Python language) - Medium", "yellow"))

def findDuplicates(numsVar):
    duplicates = lambda arr: list(set(x for x in arr if arr.count(x) > 1))
    return duplicates(numsVar)

nums = [[4,3,2,7,8,2,3,1],[1,1,2],[1]]

for test in range(len(nums)):
    print(
        colored(f"Test {(test + 1)}:", "green"),
        findDuplicates(nums[test]),
        "|",
        colored("Passed", "green")
    )