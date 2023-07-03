# Leetcode - 75. Sort Colors (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 75. Sort Colors (Python language) - Medium", "yellow"))

nums = [[2,0,2,1,1,0], [2,0,1]]

for test in range(len(nums)):

    flag = True

    while flag:
        flag = False

        for i in range(1,len(nums[test])):
            if nums[test][i-1] > nums[test][i]:
                nums[test][i-1], nums[test][i] = nums[test][i], nums[test][i-1]
                flag = True
                break
    
    testNumber = test + 1

    print(colored(f"Test {testNumber}:","green"),nums[test],"|",colored("Passed","green"))

    