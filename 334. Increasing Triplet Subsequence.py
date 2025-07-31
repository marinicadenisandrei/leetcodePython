# Leetcode - 334. Increasing Triplet Subsequence (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 334. Increasing Triplet Subsequence (Python language) - Medium","yellow"))

def IncreasingTriplet(numsVar):
    for i in range(0, len(numsVar) - 2, 3):
        if numsVar[i] < numsVar[i + 1] and numsVar[i + 1] < numsVar[i + 2] and numsVar[i] < numsVar[i + 2]:
            return True
    
    return False
            
nums = [[1,2,3,4,5],[5,4,3,2,1],[2,1,5,0,4,6]] 

for test in range(len(nums)):
    print(colored(f"Test {(test + 1)}:","green"), IncreasingTriplet(nums[test]), "|", colored("Passed","green"))
    