# Leetcode - 59. Spiral Matrix II

from termcolor import colored

print("Leetcode - 59. Spiral Matrix II")

tests = [3,1]
state = colored("Passed", "green")

for n in tests:

    copyn = n
    matrix = [[0 for _ in range(n)].copy() for _ in range(n)]

    def populate(counter):

        for i in range(len(matrix[0])):
            matrix[0][i] = counter
            counter += 1

        for i in range(1,n):
            matrix[i][-1] = counter
            counter += 1

        for i in reversed(range(n-1)):
            matrix[-1][i] = counter
            counter += 1

        for i in range(n-2,0,-1):
            matrix[i][0] = counter
            counter += 1
        
        return counter

    def removeEdges(matrixSquare):
        matrixSquare.pop(0)
        matrixSquare.pop(-1)

        for i in matrixSquare:
            i.pop(0)
            i.pop(-1)

    number = 1
    copyMatrix = []

    while len(matrix) != 0:
        try:
            number = populate(number)
            copyMatrix.append([_.copy() for _ in matrix])

            removeEdges(matrix)
            n = len(matrix)
        except IndexError:
            break

    for i in range(len(copyMatrix)):
        for j in range(1,len(copyMatrix[i])):
            copyMatrix[i][0].extend(copyMatrix[i][j])
        
        copyMatrix[i] = copyMatrix[i][:1]

    indexStart = 0

    while(len(copyMatrix) > 1):
        for i in range(len(copyMatrix[0][0])):
            if copyMatrix[0][0][i] == 0:
                copyMatrix[0][0][i] = copyMatrix[1][0][indexStart]
                indexStart += 1
        
        copyMatrix.pop(1)
        indexStart = 0

    output = []

    for i in range(copyn):
        output.append([copyMatrix[0][0][i] for i in range(copyn)])
        copyMatrix[0][0] = copyMatrix[0][0][copyn:]

    numberTest = tests.index(copyn) + 1
    text = colored(f"Test {numberTest}", "green")
    print(f"{text}: {output} | {state}")



    
        





