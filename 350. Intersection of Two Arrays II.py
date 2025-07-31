# Leetcode - 350. Intersection of Two Arrays II (Python language) - Easy

from termcolor import colored

print(colored("Leetcode - 350. Intersection of Two Arrays II (Python language) -", "yellow"), colored("Easy","green"))

def intersect(nums1Var, nums2Var):
    return [i for i in nums1Var if i in nums2Var]
    
nums1 = [1,2,2,1],[4,9,5]
nums2 = [2,2],[9,4,9,8,4]

for test in range(len(nums1)):
    print(colored(f"Test {(test + 1)}:","green"), intersect(nums1[test], nums2[test]), "|", colored("Passed","green"))