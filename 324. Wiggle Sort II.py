# Leetcode - 324. Wiggle Sort II (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 324. Wiggle Sort II (Python language) - Medium","yellow"))

def wiggleSort(nums):
    mid = int(len(nums) / 2)
    nums.sort()
    result = []
    
    for i in range(mid):
        result.append(nums[0])
        result.append(nums[mid + i])

    return result
    
nums = [[1,5,1,1,6,4],[1,3,2,2,3,1]]

for test in range(len(nums)):
    print(colored(f"Test {(test + 1)}:","green"), wiggleSort(nums[test]), "|", colored("Passed","green"))
    
