# Leetcode - 436. Find Right Interval (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 436. Find Right Interval (Python language) - Medium","yellow"))

def findRightInterval(intervalsVar):
    result = []

    for i in range(len(intervalsVar)):
        best_index = -1
        best_start = float("inf")

        for j in range(len(intervalsVar)):
            if intervalsVar[j][0] >= intervalsVar[i][1]:
                if intervalsVar[j][0] < best_start:
                    best_start = intervalsVar[j][0]
                    best_index = j

        result.append(best_index)

    return result

intervals = [[[1,2]],[[3,4],[2,3],[1,2]],[[1,4],[2,3],[3,4]]]

for test in range(len(intervals)):
    print(
        colored(f"Test {(test + 1)}:", "green"),
        findRightInterval(intervals[test]),
        "|",
        colored("Passed","green")
    )