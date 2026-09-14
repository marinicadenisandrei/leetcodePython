# Leetcode - 453. Minimum Moves to Equal Array Elements (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 453. Minimum Moves to Equal Array Elements (Python language) - Medium", "yellow"))

def minMoves(numsVar):
    numsVar.sort(reverse=True)
    result = 0

    for i in range(1, len(numsVar)):
        result += (numsVar[0] - numsVar[i])

    return result

nums = [[1,2,3],[1,1,1]]

for test in range(len(nums)):
    print(
        colored(f"Test {(test + 1)}:","green"),
        minMoves(nums[test]),
        "|",
        colored("Passed", "green")
    )
