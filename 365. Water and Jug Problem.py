# Leetcode - 365. Water and Jug Problem (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 365. Water and Jug Problem (Python language) - Medium","yellow"))

def canMeasureWater(xVar, yVar, targetVar):
    if xVar + yVar == targetVar or xVar == targetVar or yVar == targetVar:
        return True
        
    firstJug = 0
    secondJug = 0

    visited = set()

    while (firstJug, secondJug) not in visited:
        visited.add((firstJug, secondJug))

        if firstJug == targetVar or secondJug == targetVar or firstJug + secondJug == targetVar:
            return True

        if secondJug == 0:
            secondJug = yVar

        transfer = min(secondJug, xVar - firstJug)
        firstJug += transfer
        secondJug -= transfer

        if firstJug == xVar:
            firstJug = 0

    return False
            
x = [3,2,1]
y = [5,6,2]
target = [4,5,3]

for test in range(len(target)):
    print(colored(f"Test {(test + 1)}:","green"), canMeasureWater(x[test], y[test], target[test]), "|", colored("Passed","green"))