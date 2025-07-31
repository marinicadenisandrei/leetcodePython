# Leetcode - 303. Range Sum Query - Immutable (Python language) - Easy

from termcolor import colored

print(colored("Leetcode - 303. Range Sum Query - Immutable (Python language) -","yellow"), colored("Easy","green"))

class NumArray:
    def __init__(self, nums):
        self.nums = nums
    
    def sumRange(self, left, right):
        return sum(self.nums[left:right + 1])


numArray = NumArray([-2, 0, 3, -5, 2, -1])
print(colored(f"Test 1:","green"), numArray.sumRange(0,2), numArray.sumRange(2,5), numArray.sumRange(0,5), "|", colored("Passed","green"))