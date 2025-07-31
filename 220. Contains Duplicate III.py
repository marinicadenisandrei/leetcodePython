# Leetcode - 220. Contains Duplicate III (Python language) - Hard

from termcolor import colored
print(colored("Leetcode - 220. Contains Duplicate III (Python language) -", "yellow"), colored("Hard","red"))

def containsNearbyAlmostDuplicate(numsVar: list, indexDiffVar: int, valueDiffVar: int):
    for i in range(len(numsVar)):
        for j in range(len(numsVar)):
            if i != j and abs(i - j) <= indexDiffVar and abs(numsVar[i] - numsVar[j]) <= valueDiffVar:
                return True
    return False            

nums = [[1,2,3,1],[1,5,9,1,5,9]]
indexDiff = [3,2]
valueDiff = [0,3]

for test in range(len(nums)):
    print(colored(f"Test {(test + 1)}:","green"), containsNearbyAlmostDuplicate(nums[test], indexDiff[test], valueDiff[test]), "|", colored("Passed","green"))