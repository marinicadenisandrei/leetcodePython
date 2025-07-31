# Leetcode - 283. Move Zeroes (Python language) - Easy

from termcolor import colored

print(colored("Leetcode - 283. Move Zeroes (Python language) -","yellow"), colored("Easy", "green"))

def moveZeroes(numsVar):
    non_zero_elements = [item for item in numsVar if item != 0]
    non_zero_elements.extend([0] * numsVar.count(0))
    return non_zero_elements

nums = [[0,1,0,3,12],[0]]

for test in range(len(nums)):
    print(colored(f"Test {(test + 1)}:", "green"), moveZeroes(nums[test]), "|", colored("Passed", "green"))
