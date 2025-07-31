# Leetcode - 56. Insert Intervals
print("56. Insert Intervals")

from termcolor import colored

intervalsTest = [[[1,3],[6,9]],[[1,2],[3,5],[6,7],[8,10],[12,16]]]
newIntervalTest = [[2,5],[4,8]]

state = colored("Passed","green")

for test in range(len(intervalsTest)):
    intervals = intervalsTest[test]
    newInterval = newIntervalTest[test]

    intervals.extend([newInterval])
    intervals.sort()

    flag = True
    flagRestart = False

    while flag:
        flagRestart = False

        for i in range(len(intervals)):
            try:
                for j in range(i+1,i+2):
                    firstRange = [_ for _ in range(intervals[i][0],intervals[i][-1]+1)]
                    secondRange = [_ for _ in range(intervals[j][0],intervals[j][-1]+1)]

                    intersection = [_ for _ in firstRange if _ in secondRange]
                    
                    if len(intersection) > 0:
                        firstRange.extend(secondRange)
                        firstRange.sort()

                        intervals[j] = [firstRange[0], firstRange[-1]]
                        intervals.pop(i)
                        flagRestart = True

            except IndexError:
                flag = False
                flagRestart = True

            firstRange = []
            secondRange = []

            if flagRestart: break

    noTest = test+1
    text = colored(f"Test {noTest}: ", "green")

    print(f"{text}{intervals} | {state}")

