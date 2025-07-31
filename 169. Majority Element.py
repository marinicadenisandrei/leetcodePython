# Leetcode - 169. Majority Element (Python language) - Easy

from termcolor import colored

print(colored("Leetcode - 169. Majority Element (Python language) -", "yellow"), colored("Easy","green"))

def majorityElement(numsVar:list):
    return max(set(numsVar), key=lambda x: numsVar.count(x))

nums = [[3,2,3],[2,2,1,1,1,2,2]]

for test in range(len(nums)):
    print(colored(f"Test {(test + 1)}:","green"),majorityElement(nums[test]),"|",colored("Passed","green"))