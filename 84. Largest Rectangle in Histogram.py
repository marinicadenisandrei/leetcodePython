# Leetcode - 84. Largest Rectangle in Histogram (Python language) - Hard

from termcolor import colored

print(colored("Leetcode - 84. Largest Rectangle in Histogram (Python language) -", "yellow"), colored("Hard", "red"))

heightsTest = [[2,1,5,6,2,3], [2,4]]

for test in heightsTest:
    heights = test
    output = []
    
    maxHeights = max(heights)

    for i in range(len(heights)):
        output.append([])
        for j in range(maxHeights):
            if j < heights[i]:
                output[i].append("X")
            else:
                output[i].append("0")

    temp = []
    area = []

    sumVar = 0

    for i in range(len(output)):
        for j in range(len(output)):
            if output[j][i] == "X":
                sumVar += i + 1
            else:
                area.append(sumVar)
                sumVar = 0
                temp.append("X")

        if len(temp) == 0:
            area.append(sumVar)
            sumVar = 0

        temp = []

    testNumber = heightsTest.index(test) + 1

    print(colored(f"Test {testNumber}:", "green") ,max(area), "|", colored(f"Passed","green"))