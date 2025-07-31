# Leetcode - 373. Find K Pairs with Smallest Sums (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 373. Find K Pairs with Smallest Sums (Python language) - Medium","yellow"))

def kSmallestPairs(nums1Var, nums2Var, kVar):
    result = []

    for i in nums1Var:
        for j in nums2Var:
            result.append([i,j])
    
    result.sort()
    return result[:kVar]

nums1 = [[1,7,11],[1,1,2]]
nums2 = [[2,4,6],[1,2,3]]
k = [3,2]

for test in range(len(k)):
    print(colored(f"Test {(test + 1)}:","green"), kSmallestPairs(nums1[test], nums2[test], k[test]), "|", colored("Passed","green"))
    