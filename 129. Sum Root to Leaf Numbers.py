# Leetcode - 129. Sum Root to Leaf Numbers (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 129. Sum Root to Leaf Numbers (Python language) - Medium", "yellow"))

def sumNumbers(rootVar: list):
    if len(rootVar) <= 3:
        return int(str(rootVar[0]) + str(rootVar[1])) + int(str(rootVar[0]) + str(rootVar[2]))

    varWhile = len(rootVar)
    powerVar = 1
    counter = 0

    while(varWhile > 0):
        varWhile -= powerVar
        powerVar *= 2
        counter += 1
    
    # for _ in range(abs(varWhile)): rootVar.append(0)
    indexList = [[] for _ in range(counter)]

    indexElement = 0
    divVar = counter + 1

    for i in range(len(indexList)):
        factor = 0
        for j in range(counter + 1):
            if factor == divVar:
                indexElement += 1
                factor = 0
            factor += 1
            
            indexList[i].append(indexElement)

        indexElement += 1
        divVar /= 2

    stringVar = ""
    globalNumber = 0
    counter = 0

    for i in range(len(indexList[0])):
        for j in range(len(indexList)):
            try:
                stringVar += str(rootVar[indexList[j][counter]])
            except IndexError:
                globalNumber += int(stringVar)
                return globalNumber
        
        counter += 1
        globalNumber += int(stringVar)
        stringVar = ""

    return globalNumber
            
    
root = [[1,2,3],[4,9,0,5,1]]

for test in range(len(root)):
    print(colored(f"Test {(test + 1)}:", "green"),sumNumbers(root[test]), "|", colored("Passed", "green"))