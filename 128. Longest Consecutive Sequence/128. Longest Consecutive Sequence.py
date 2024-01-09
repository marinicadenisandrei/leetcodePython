# Leetcode - 128. Longest Consecutive Sequence (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 128. Longest Consecutive Sequence (Python language) - Medium","yellow"))

def longestConsecutive(numsVar: list):
    numsVar.sort()
    result = 0
    temp = 1

    for i in range(1,len(numsVar)):
        if numsVar[i] - numsVar[i-1] == 1:
            temp += 1
        else:
            if temp > result:
                result = temp
            
            temp = 1
    
    return result
                
        

nums = [[100,4,200,1,3,2], [0,3,7,2,5,8,4,6,0,1]]

for test in range(len(nums)):
    print(colored(f"Test {(test + 1)}:", "green"), longestConsecutive(nums[test]), "|", colored("Passed", "green"))