# Leetcode - 456. 132 Pattern (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 456. 132 Pattern (Python language) - Medium", "yellow"))

def find132pattern(nums):
    stack = []
    second = float('-inf')

    for num in reversed(nums):
        if num < second:
            return True

        while stack and num > stack[-1]:
            second = stack.pop()

        stack.append(num)

    return False

nums = [[1,2,3,4],[3,1,4,2],[-1,3,2,0]]

for test in range(len(nums)):
    print(
        colored(f"Test {(test + 1)}:", "green"),
        find132pattern(nums[test]),
        "|",
        colored("Passed", "green")
    )