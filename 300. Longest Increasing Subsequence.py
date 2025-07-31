# Leetcode - 300. Longest Increasing Subsequence (Python language) - Medium 

from termcolor import colored

print(colored("Leetcode - 300. Longest Increasing Subsequence (Python language) - Medium","yellow"))

def lengthOfLIS(numsVar):
    maxVar = 0

    for j in range(len(numsVar)):
        counter = 0

        for i in range(j, len(numsVar) - 1):
            if numsVar[i] < numsVar[i + 1]:
                counter += 1
        
        if maxVar < counter:
            maxVar = counter
            
    return maxVar + 1
                
nums = [[10,9,2,5,3,7,101,18], [0,1,0,3,2,3], [7,7,7,7,7,7,7]]

for test in range(len(nums)):
    print(colored(f"Test {(test + 1)}:","green"), lengthOfLIS(nums[test]), "|", colored("Passed","green"))
