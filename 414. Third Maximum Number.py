# Leetcode - 414. Third Maximum Number (Python language) - Easy

from termcolor import colored

print(colored("Leetcode - 414. Third Maximum Number (Python language) -","yellow"), colored("Easy","green"))

def thirdMax(numsVar):
    numsVar = list(dict.fromkeys(numsVar))
    sorted(numsVar, reverse=True)

    try:
        return numsVar[2]
    except IndexError:
        return numsVar[-1]

nums = [[3,2,1],[1,2],[2,2,3,1]]

for test in range(len(nums)):
    print(
        colored(f"Test {(test + 1)}:", "green"),
        thirdMax(nums[test]),
        "|",
        colored("Passed","green")
    )