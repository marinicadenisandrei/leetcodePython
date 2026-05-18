# Leetcode - 435. Non-overlapping Intervals (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 435. Non-overlapping Intervals (Python language) - Medium", "yellow"))

def eraseOverlapIntervals(intervalsVar):
    intervalsVar.sort(key=lambda x: x[0])

    result = 0
    previous_end = intervalsVar[0][1]

    for i in range(1, len(intervalsVar)):
        current_start = intervalsVar[i][0]
        current_end = intervalsVar[i][1]

        if current_start < previous_end:
            result += 1
            previous_end = min(previous_end, current_end)
        else:
            previous_end = current_end

    return result


intervals = [[[1,2],[2,3],[3,4],[1,3]],[[1,2],[1,2],[1,2]],[[1,2],[2,3]]]

for test in range(len(intervals)):
    print(
        colored(f"Test {(test + 1)}:", "green"),
        eraseOverlapIntervals(intervals[test]),
        "|",
        colored("Passed", "green")
    )
