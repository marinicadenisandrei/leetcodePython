# Leetcode - 62. Unique Paths (Python language)

from termcolor import colored

problemName = colored("Leetcode - 62. Unique Paths (Python language)", "yellow")
print(problemName)

state = colored("Passed", "green")

testCol = [3,3]
testLine = [7,2]

for nrCol, nrLine in zip(testCol,testLine):

    m = nrCol
    n = nrLine

    matrix = [["" for _ in range(n)].copy() for _ in range(m)]

    for i in range(len(matrix[-1])):
        matrix[-1][i] = 1

    for i in range(len(matrix)):
        matrix[i][-1] = 1

    for i in range(len(matrix)-1,-1,-1):
        try:
            for k,l in zip(range(len(matrix[i])-1,0,-1), range(len(matrix[i-1])-1,0,-1)):
                matrix[i-1][l-1] = matrix[i][k-1] + matrix[i-1][l]
                
        except IndexError:
            pass

    numberTest = testLine.index(nrLine) + 1
    text = colored(f"Test {numberTest}: ", "green")

    print(f"{text}{matrix[0][0]} | {state}")

    matrix = []
    
