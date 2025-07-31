# Leetcode - 215. Kth Largest Element in an Array (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 215. Kth Largest Element in an Array (Python language) - Medium","yellow"))

def findKthLargest(numsVar: list, kVar: int):
    numsVar.sort(reverse=True)
    return numsVar[kVar - 1]
    
nums = [[3,2,1,5,6,4],[3,2,3,1,2,4,5,5,6]]
k = [2,4]

for test in range(len(k)):
    print(colored(f"Test {(test + 1)}:","green"), findKthLargest(nums[test], k[test]), "|", colored("Passed","green"))