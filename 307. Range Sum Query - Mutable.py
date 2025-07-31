# Leetcode - 307. Range Sum Query - Mutable (Python language) - Medium

from termcolor import colored
print(colored("# Leetcode - 307. Range Sum Query - Mutable (Python language) - Medium","yellow"))

class NumArray:
    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, start, end):
        return sum(self.nums[start:end + 1])
    
    def update(self, index, element):
        self.nums[index] = element
        return self.nums

numArray = NumArray([1,3,5])
print(colored("Test 1:", "green"), numArray.sumRange(0, 2), numArray.update(1, 2), numArray.sumRange(0, 2), "|", colored("Passed","green"))


