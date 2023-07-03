# Leetcode - 64. Minimum Path Sum (Python language)

from termcolor import colored

print(colored("Leetcode - 64. Minimum Path Sum (Python language)", "yellow"))

state = colored("Passed", "green")

testGrids = [[[1,3,1],[1,5,1],[4,2,1]],
        [[1,2,3],[4,5,6]]]

for test in testGrids:

    grid = test

    for i in range(1,len(grid[0])):
        grid[0][i] = grid[0][i-1] + grid[0][i]

    for i in range(1,len(grid)):
        grid[i][0] = grid[i-1][0] + grid[i][0]

    for i in range(1,len(grid)):
        for j in range(1,len(grid[i])):
            grid[i][j] = grid[i][j] + min(grid[i][j-1], grid[i-1][j])
    
    testNumber = testGrids.index(test) + 1
    text = colored(f"Test {testNumber}: ", "green")
    result = grid[-1][-1]

    print(f"{text}{result} | {state}")
