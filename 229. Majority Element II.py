# Leetcode - 229. Majority Element II (Python language) - Medium

from termcolor import colored
print(colored("Leetcode - 229. Majority Element II (Python language) - Medium","yellow"))

def majorityElement(numsVar):
    candidates = []

    for i in range(len(numsVar)):
        candidates.append(numsVar.count(numsVar[i]))
    
    maxValue = max(candidates)
    return list(dict.fromkeys([numsVar[i] for i in range(len(numsVar)) if numsVar.count(numsVar[i]) == maxValue]))
    
nums = [[3,2,3],[1],[1,2]]

for test in range(len(nums)):
    print(colored(f"Test {(test + 1)}:","green"), majorityElement(nums[test]), "|", colored("Passed","green"))