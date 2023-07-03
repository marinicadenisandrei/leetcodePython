# Leetcode - 63. Unique Paths II (Python Language)

from termcolor import colored

print(colored("Leetcode - 63. Unique Paths II (Python Language)", "yellow"))

state = colored("Passed", "green")

testGrids = [[[0,0,0],[0,1,0],[0,0,0]], [[0,1],[0,0]]]

for test in testGrids:

    obstacleGrid = test

    for i in obstacleGrid:
        for j in range(len(i)):
            if i[j] == 1: i[j] = "X";

    for i in range(len(obstacleGrid[-1])):
        if obstacleGrid[-1][i] == 0 : obstacleGrid[-1][i] = 1

    for i in range(len(obstacleGrid)):
        if obstacleGrid[i][-1] == 0: obstacleGrid[i][-1] = 1

    for i in range(len(obstacleGrid)-1,-1,-1):
        try:
            for k,l in zip(range(len(obstacleGrid[i])-1, 0, -1), range(len(obstacleGrid[i-1])-1, 0, -1)):
                if obstacleGrid[i-1][k-1] != 'X':
                    try:
                        obstacleGrid[i-1][k-1] = obstacleGrid[i][k-1] + obstacleGrid[i-1][k]
                    except TypeError:
                        try:
                            obstacleGrid[i-1][k-1] = obstacleGrid[i][k-1] + 0
                        except TypeError:
                            obstacleGrid[i-1][k-1] = 0 + obstacleGrid[i-1][k]
        except IndexError:
            pass
    
    numberTest = testGrids.index(test) + 1
    text = colored(f"Test {numberTest}: ", "green")
    print(f"{text}{obstacleGrid[0][0]} | {state}")
