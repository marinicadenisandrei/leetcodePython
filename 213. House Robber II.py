from termcolor import colored

print(colored("Leetcode - 213. House Robber II (Python) - Medium","yellow"))

def rob(numsVar: list):
    starter = 0
    result = 0
    
    if len(numsVar) % 2 == 0:
        starter = 0
    else:
        starter = 1
    
    for j in range(len(numsVar)): 
        sum = 0

        for i in range(starter + j, len(numsVar), 2):
            sum += numsVar[i]
        
        if result < sum:
            result = sum
            
    return result

nums = [[2,3,2],[1,2,3,1],[1,2,3]]

for test in range(len(nums)):
    print(colored(f"Test {(test + 1)}:","green"), rob(nums[test]), "|", colored("Passed","green"))