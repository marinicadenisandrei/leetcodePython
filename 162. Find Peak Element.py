# Leetcode - 162. Find Peak Element (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 162. Find Peak Element (Python language) - Medium","yellow"))

def findPeakElement(numsVar: list):
    acumulation = []

    for i in range(1,len(numsVar)):
        if numsVar[i - 1] < numsVar[i] and numsVar[i] > numsVar[i + 1]:
            acumulation.append(i)
    
    return max(acumulation)
    
nums = [[1,2,3,1],[1,2,1,3,5,6,4]]

for test in range(len(nums)):
    print(colored(f"Test {(test + 1)}:","green"),findPeakElement(nums[test]),"|",colored("Passed","green"))