# Leetcode - 413. Arithmetic Slices (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 413. Arithmetic Slices (Python language) - Medium","yellow"))

def numberOfArithmeticSlices(numsVar):
    total = 0
    result = 0

    for i in range(0, len(numsVar) - 1):
        if numsVar[i + 1] - numsVar[i] == 1:
            total += 1
    
    if total >= 2:
        result += 1
        result += len(numsVar) - 2
    
    return result

nums = [[1,2,3,4],[1]]

for test in range(len(nums)):
    print(
        colored(f"Test {(test + 1)}:","green"),
        numberOfArithmeticSlices(nums[test]),
        "|",
        colored("Passed","green")
    )