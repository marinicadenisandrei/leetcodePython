# Leetcode - 73. Set Matrix Zeroes (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 73. Set Matrix Zeroes (Python language) - Medium", "yellow"))

state = colored("Passed", "green")

matrixTest = [[[1,1,1],[1,0,1],[1,1,1]], [[0,1,2,0],[3,4,5,2],[1,3,1,5]]]

def makeZeroCol(list, colNumber):
    for i in range(len(list[0])):
        for j in range(len(list)):
            if i == colNumber:
                list[j][i] = 0

def makeZeroRow(list, rowNumber):    
    for i in range(len(list)):
        if i == rowNumber:
            list[i] = [0] * len(list[i])


for test in matrixTest:
    matrix = test

    removeElements = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                removeElements.append((i,j))

    for i in removeElements:
        makeZeroRow(matrix,i[0])
        makeZeroCol(matrix,i[1])

    testNumber = matrixTest.index(test) + 1
    text = colored(f"Test {testNumber}: ","green")

    print(f"{text}{matrix} | {state}")


