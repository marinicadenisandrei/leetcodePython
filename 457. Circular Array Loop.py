# Leetcode - 457. Circular Array Loop (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 457. Circular Array Loop (Python language) - Medium","yellow"))

def circularArrayLoop(numsVar):
    return len(numsVar) != len(list(dict.fromkeys(numsVar)))

nums = [[2,-1,1,2,2],[-1,-2,-3,-4,-5,6],[1,-1,5,1,4]]

for test in range(len(nums)):
    print(
        colored(f"Test {(test + 1)}:", "green"),
        circularArrayLoop(nums[test]),
        "|",
        colored("Passed","green")
    )