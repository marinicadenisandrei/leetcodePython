# Leetcode - 377. Combination Sum IV (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 377. Combination Sum IV (Python language) - Medium","yellow"))

def combinationSum4(nums, target):
    dp = [0] * (target + 1)
    dp[0] = 1
    
    for s in range(1, target + 1):
        for num in nums:
            if s >= num:
                dp[s] += dp[s - num]
    
    return dp[target]


nums = [[1,2,3],[9]]
target = [4,3]

for test in range(len(nums)):
    print(colored(f"Test {(test + 1)}:","green"), combinationSum4(nums[test], target[test]), "|", colored("Passed","green"))

