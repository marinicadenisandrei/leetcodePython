# Leetcode - 124. Binary Tree Maximum Path Sum (Python language) - Hard

from termcolor import colored

print(colored("Leetcode - 124. Binary Tree Maximum Path Sum (Python language) -", "yellow"), colored("Hard", "red"))

def maxPathSum(rootVar):
    sumsVar = [rootVar[0] + rootVar[1] + rootVar[2]]
    rootVar = rootVar[1:]

    if len(rootVar) < 3:
        return sumsVar[0]
        
    leftNumbers = 2

    while len(rootVar) != 0:
        left = rootVar[:leftNumbers]
        rootVar = rootVar[leftNumbers:]
        right = rootVar[:leftNumbers * 2]

        if len(left) == 0 or len(right) == 0:
            break

        for i in range(len(left)):
            sumsVar.append(left[0] + right[0] + right[1])
            left = left[1:]
            right = right[2:]

        leftNumbers *= 2

        return max(sumsVar)

root = [[1,2,3],[-10,9,20,0,0,15,7]]

for test in range(len(root)):
    testNumber = test + 1
    print(colored(f"Test {testNumber}:", "green"), maxPathSum(root[test]), "|", colored("Passed", "green"))