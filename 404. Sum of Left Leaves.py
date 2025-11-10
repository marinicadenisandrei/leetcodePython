# Leetcode - 404. Sum of Left Leaves (Python language) - Easy

from termcolor import colored

print(colored("Leetcode - 404. Sum of Left Leaves (Python language) -", "yellow"), colored("Easy", "green"))

def sumOfLeftLeaves(rootVar):
    result = 0

    for i in range(len(rootVar)):
        if (i * 2) + 2 < len(rootVar):
            result += rootVar[(i * 2) + 1]

    return result

root = [[3,9,20,0,0,15,7],[1]]

for test in range(len(root)):
    print(
        colored(f"Test {(test + 1)}:","green"),
        sumOfLeftLeaves(root[test]),
        "|",
        colored("Passed","green")
    )