# Leetcode - 217. Contains Duplicate (Python language) - Easy 

from termcolor import colored
print(colored("Leetcode - 217. Contains Duplicate (Python language) -","yellow"),colored("Easy","green"))

def containsDuplicate(numsVar: list):
    if len(numsVar) != len(list(dict.fromkeys(numsVar))):
        return True
    
    return False
        
nums = [[1,2,3,1],[1,2,3,4],[1,1,1,3,3,4,3,2,4,2]]

for test in range(len(nums)):
    print(colored(f"Test {(test + 1)}:","green"),containsDuplicate(nums[test]),"|", colored("Passed","green"))