# Leetcode - 287. Find the Duplicate Number (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 287. Find the Duplicate Number (Python language) - Medium","yellow"))

def findDuplicate(numsVar):
    for i in numsVar:
        if numsVar.count(i) > 1:
            return i
            
nums = [[1,3,4,2,2],[3,1,3,4,2],[3,3,3,3,3]]

for test in range(len(nums)):
    print(colored(f"Test {(test + 1)}:", "green"), findDuplicate(nums[test]), "|", colored("Passed","green"))