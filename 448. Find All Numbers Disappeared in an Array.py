# Leetcode - 448. Find All Numbers Disappeared in an Array (Python language) - Easy

from termcolor import colored

print(colored("Leetcode - 448. Find All Numbers Disappeared in an Array (Python language) -", "yellow"), colored("Easy", "green"))

def findDisappearedNumbers(numsVar):
    seen = set(numsVar)
    return [i for i in range(1, len(numsVar) + 1) if i not in seen]

nums = [[4,3,2,7,8,2,3,1],[1,1]]

for test in range(len(nums)):
    print(
        colored(f"Test {(test + 1)}:", "green"),
        findDisappearedNumbers(nums[test]),
        "|",
        colored("Passed", "green")
    ) 