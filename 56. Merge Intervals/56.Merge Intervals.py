# Leetcode - 55. Merge Intervals
print("\n55.Merge Intervals\n")

from termcolor import colored

testIntervals = [[[1,3],[2,6],[8,10],[15,18]],[[1,4],[4,5]]]
flag = True
intersection = []
concatenation = []
state = colored("Passed", "green")

for test in testIntervals:
    intervals = test
    for i in range(len(intervals)):
        try:
            for j in range(i+1,i+2):

                intervals[i] = [_ for _ in range(intervals[i][0],intervals[i][-1]+1)]
                intervals[j] = [_ for _ in range(intervals[j][0],intervals[j][-1]+1)]

                intersection = [_ for _ in intervals[i] if _ in intervals[j]]

                if len(intersection) > 0:
                    concatenation = intervals[i] + intervals[j]
                    concatenation.sort()
                    intervals[j] = [concatenation[0], concatenation[-1]]
                    intervals.remove(intervals[i])
        except IndexError:
            break

    intervals = [[i[0],i[-1]] if len(i) > 2 else i for i in intervals ]
    indexTest = testIntervals.index(test) + 1
    text = colored(f"Test {indexTest}: ", "green")
    print(f"{text} {intervals} | {state}")

print("\n")

