from termcolor import colored

print(colored("Leetcode - 80. Remove Duplicates from Sorted Array II (Python language) - Medium","yellow"))

numsTest = [[1,1,1,2,2,3], [0,0,1,1,1,1,2,3,3]]

for test in numsTest:
    nums = test
    for i in nums:
        if nums.count(i) > 2:
            for j in range(nums.count(i) - 2):
                nums.remove(i)
                nums.append("_")

    testNumber = numsTest.index(test) + 1

    print(colored(f"Test {testNumber}:","green"), len([_ for _ in nums if _ != "_"]),nums, "|", colored("Passed","green"))