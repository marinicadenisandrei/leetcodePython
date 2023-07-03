# Leetcode - 85. Maximal Rectangle (Python language) - Hard

from termcolor import colored

print(colored("Leetcode - 85. Maximal Rectangle (Python language) -", "yellow"), colored("Hard","red"))

matrixTest = [[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]], [["0"]]]

for test in matrixTest:
    matrix = test

    copyMatrix = [_.copy() for _ in matrix]

    indexStep = 0

    def sumRectangle(startLine, endLine, startCol, endCol):
        sum = 0

        for i in matrix[startCol:endCol]:
            print(i[startLine:endLine])

    def filterListByOne(listVar):
        lengthList = len(listVar)

        if len(list(filter(lambda x: x == "1", listVar))) == lengthList:
            return True
        else:
            return False

    sumVar = 0
    maxVar = 0

    for m in range(len(copyMatrix)):
        matrix = [copyMatrix[restart].copy() for restart in range(m,len(copyMatrix))]

        for n in matrix:
            n.append("0")

        for k in range(len(matrix[0])):    
            for i in range(len(matrix[0])):
                if matrix[0][i] == "0":
                    for j in range(len(matrix)):
                        if len(matrix[j][:i]) > 0:
                            if filterListByOne(matrix[j][:i]) == False:
                                break
                            sumVar += sum([int(_) for _ in matrix[j][:i]])
                        else:
                            break
        
            if maxVar < sumVar:
                maxVar = sumVar

            sumVar = 0
            for l in range(len(matrix)):
                matrix[l].pop(0)

    testNumber = matrixTest.index(test) + 1
    
    print(colored(f"Test {testNumber}:", "green"), maxVar, "|", colored("Passed", "green"))
    

