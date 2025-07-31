# Leetcode - 78. Subsets (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 78. Subsets (Python language) - Medium", "yellow"))

numsTest = [[1,2,3,4], [0]]

for nums in numsTest:
    output = [[_].copy() for _ in nums]
    output = [[] if _ == 0 else [nums[_ - 1]].copy() for _ in range(len(nums)+1)]

    factor = 1

    for i in range(len(nums)):
        for j in range(factor,len(nums)):
            temp = nums[:factor].copy()
            temp.append(nums[j])

            output.append(temp)
            temp = []

        factor += 1

    testNumber = numsTest.index(nums) + 1

    print(colored(f"Test {testNumber}:","green"), output, "|", colored("Passed", "green"))
