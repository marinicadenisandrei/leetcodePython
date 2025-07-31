# Leetcode 238. Product of Array Except Self (Python language) - Medium

from termcolor import colored

print(colored("Leetcode 238. Product of Array Except Self (Python language) - Medium","yellow"))

def productExceptSelf(numsVar):
    product = 1
    results = []

    for i in range(len(numsVar)):
        for j in range(len(numsVar)):
            if i != j:
                product *= numsVar[j]
        
        results.append(product)
        product = 1
                
    return results

nums = [[1,2,3,4], [-1,1,0,-3,3]]

for test in range(len(nums)):
    print(colored(f"Test {(test + 1)}:","green"), productExceptSelf(nums[test]), "|", colored("Passed","green"))