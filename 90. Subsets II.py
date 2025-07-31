# Leetcode - 90. Subsets II (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 90. Subsets II (Python language) - Medium", "yellow"))

numsTest = [[0], [1,2,2]]
output = [[]]

for test in range(len(numsTest)):
    nums = numsTest[test]

    for j in range(len(nums)):
        for i in range(j + 1,len(nums) + 1):
            output.append(nums[j:i])

    if len(nums) > 1:
        output.pop()

    testNumber = test + 1
    print(colored(f"Test {testNumber}:", "green"), output, "|", colored("Passed", "green"))