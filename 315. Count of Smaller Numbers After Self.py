# Leetcode - 315. Count of Smaller Numbers After Self (Python language) - Hard

from termcolor import colored

print(colored("Leetcode - 315. Count of Smaller Numbers After Self (Python language) -","yellow"), colored("Hard","red"))

def countSmaller(numsVar):
    results = []

    for i in range(len(numsVar)):
        results.append(len([x for x in numsVar[i:] if x < numsVar[i]]))

    return results

nums = [[5,2,6,1],[-1],[-1,-1]]

for test in range(len(nums)):
    print(colored(f"Test {(test + 1)}:","green"), countSmaller(nums[test]), "|", colored("Passed","green"))