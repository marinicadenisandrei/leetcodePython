# Leetcode - 198. House Robber (Python language) - Medium

from termcolor import colored
print(colored("Leetcode - 198. House Robber (Python language) - Medium","yellow"))

def rob(numsVar : list):
    maxVar = 0  
    sum = 0
    for i in range(2):
        for j in range(i,len(numsVar),2):
            sum += numsVar[j]
        
        if maxVar < sum:
            maxVar = sum
        
        sum = 0
    
    return maxVar

nums = [[1,2,3,1],[2,7,9,3,1]]

for test in range(len(nums)):
    print(colored(f"Test {(test + 1)}:", "green"), rob(nums[test]), "|", colored("Passed", "green"))