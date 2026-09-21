# Leetcode - 454. 4Sum II (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 454. 4Sum II (Python language) - Medium", "yellow"))

def fourSumCount(nums1Var, nums2Var, nums3Var, nums4Var):
    sums = {}

    for i in nums1Var:
        for j in nums2Var:
            total = i + j

            if total in sums:
                sums[total] += 1
            else:
                sums[total] = 1

    count = 0

    for i in nums3Var:
        for j in nums4Var:
            total = i + j
            opposite = -total

            if opposite in sums:
                count += sums[opposite]

    return count

nums1 = [[1,2],[0]]
nums2 = [[-2,-1],[0]]
nums3 = [[-1,2],[0]]
nums4 = [[0,2],[0]]

for test in range(len(nums1)):
    print(
        colored(f"Test {(test + 1)}:", "green"),
        fourSumCount(nums1[test], nums2[test], nums3[test], nums4[test]),
        "|",
        colored("Passed", "green")
    )