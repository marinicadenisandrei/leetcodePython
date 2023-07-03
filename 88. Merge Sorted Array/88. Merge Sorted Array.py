# Leetcode - 88. Merge Sorted Array (Python language) - Easy

from termcolor import colored

print(colored("Leetcode - 88. Merge Sorted Array (Python language) -", "yellow"), colored("Easy", "green"))

nums1 = [[1,2,3,0,0,0], [1], [0]]
m = [3,1,0] 

nums2 = [[2,5,6], [], [1]]
n = [3,0,1]

for test in range(len(nums1)):
    nums1[test] = nums1[test][:m[test]]
    nums1[test].extend(nums2[test][:n[test]])

    testNumber = test + 1
    
    print(colored("Test {testNumber}:", "green"), nums1[test], "|", colored("Passed", "green"))

