# Leetcode - 108. Convert Sorted Array to Binary Search Tree (Python language) - Easy

from termcolor import colored

print(colored("Leetcode - 108. Convert Sorted Array to Binary Search Tree (Python language) -", "yellow"), colored("Easy", "green"))

numsTest = [[-10,-3,0,5,9], [1,3]]

for test in range(len(numsTest)):
    nums = numsTest[test]

    mid = int((len(nums) - 1) / 2)
    output = []

    if len(nums) < 3:
        output = [nums[mid + 1], nums[mid]]

    else:
        output = [nums[mid], nums[mid-1], nums[-1]]

        for i,j in zip(reversed(nums[:mid - 1]), reversed(nums[mid + 1:-1])):
            output.append(i)
            output.append(0)

            output.append(j)
            output.append(0)

    testNumber = test + 1

    print(colored(f"Test {testNumber}:", "green"), output, "|", colored("Passed", "green"))





