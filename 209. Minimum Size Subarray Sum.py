# Leetcode - 209. Minimum Size Subarray Sum (Python language) - Medium

from termcolor import colored
print(colored("Leetcode - 209. Minimum Size Subarray Sum (Python language) - Medium","yellow"))

def minSubArrayLen(targetVar: int, numsVar: list):
    results = []

    for i in range(len(numsVar)):
        sum = 0
        count = 0

        for j in range(i,len(numsVar)):
            count += 1
            sum += numsVar[j]

            if sum == targetVar:
                results.append(count)
                break
            elif sum > targetVar:
                break
    
    if len(results) == 0:
        return 0
        
    return min(results)
                

target = [7,4,11]
nums = [[2,3,1,2,4,3],[1,4,4],[1,1,1,1,1,1,1,1]]

for test in range(len(target)):
    print(colored(f"Test {(test + 1)}:","green"), minSubArrayLen(target[test], nums[test]), "|", colored("Passed","green"))