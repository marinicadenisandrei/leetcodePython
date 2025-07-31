# Leetcode - 260. Single Number III (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 260. Single Number III (Python language) - Medium",'yellow'))

def singleNumber(numsVar):
    result = []

    for i in list(dict.fromkeys(numsVar)):
        if numsVar.count(i) == 1:
            result.append(i)
    
    return result 
    

nums = [[1,2,1,3,2,5],[-1,0],[0,1]]

for test in range(len(nums)):
    print(colored(f"Test {(test + 1)}:","green"), singleNumber(nums[test]), "|", colored("Passed","green"))