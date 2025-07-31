# Leetcode - 239. Sliding Window Maximum (Python language) - Hard

from termcolor import colored
print(colored("Leetcode - 239. Sliding Window Maximum (Python language) -","yellow"), colored("Hard","red"))

def maxSlidingWindow(numsVar, kVar):
    return [max(numsVar[i:i + kVar]) for i in range(len(numsVar) - kVar + 1)]
        
nums = [[1,3,-1,-3,5,3,6,7],[1]]
k = [3,1]

for test in range(len(k)):
    print(colored(f"Test {(test + 1)}: ","green"), maxSlidingWindow(nums[test], k[test]), "|", colored("Passed","green"))