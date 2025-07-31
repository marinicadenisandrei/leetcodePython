# Leetcode - 228. Summary Ranges (Python language) - Easy

from termcolor import colored

print(colored("Leetcode - 228. Summary Ranges (Python language) -","yellow"), colored("Easy","green"))

def summaryRanges(numsVar):
    ranges = []
    start = 0
    numsVar.append(0)

    for i in range(len(numsVar) - 1):
        if abs(numsVar[i] - numsVar[i + 1]) > 1:
            if start != i:
                ranges.append(str(numsVar[start]) + "->" + str(numsVar[i]))
            else:
                ranges.append(str(numsVar[start]))
            
            start = i + 1

    return ranges
            
        

nums = [[0,1,2,4,5,7],[0,2,3,4,6,8,9]]

for test in range(len(nums)):
    print(colored(f"Test {(test + 1)}:", "green"), summaryRanges(nums[test]), "|", colored("Passed","green"))