# Leetcode - 437. Path Sum III (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 437. Path Sum III (Python language) - Medium", "yellow"))

def pathSum(rootVar, targetSumVar):
    result = 0
    acumulation = []

    level = 0
    length = len(rootVar)
    
    while length > 1:
        level += 1
        length /= 2
    
    counter = 0
    step = level * 2
    index = 0

    for i in range(level):
        tempList = []

        for j in range(level * 2):
            if counter >= step:
                index += 1
                counter = 0

            try:
                tempList.append(rootVar[index])
            except IndexError:
                tempList.append(0)

            counter += 1
        
        acumulation.append(tempList)
        step /= 2
    
    used = []

    for k in range(len(acumulation[0]) - 1):
        for i in range(len(acumulation[0])):
            tempSum = 0
            usedTemp = []

            for j in range(k, len(acumulation)):
                tempSum += acumulation[j][i]
                usedTemp.append(acumulation[j][i])

                if acumulation[j][i] == 0:
                    continue

                if tempSum == targetSumVar and usedTemp not in used:
                    result += 1
                    used.append(usedTemp)
                    break
    
    return result
    
root = [[10,5,-3,3,2,0,11,3,-2,0,1],[5,4,8,11,0,13,4,7,2,0,0,5,1]]
targetSum = [8,22]

for test in range(len(root)):
    print(
        colored(f"Test {(test + 1)}:", "green"),
        pathSum(root[test], targetSum[test]),
        "|",
        colored("Passed", "green")
    )