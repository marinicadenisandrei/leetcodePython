# Leetcode - 218. The Skyline Problem (Python language) - Hard 

from termcolor import colored
print(colored("Leetcode - 218. The Skyline Problem (Python language) -","yellow"), colored("Hard", "red"))

def populateWithOnes(building, matrix):
    for i in range(building[2]):
        for j in range(building[0],building[1] + 1):
            matrix[i][j] = 1
        
def getSkyline(buildingsVar: list):
    acumulation = []
    orizontal = 0
    vertical = 0
    result = []

    for i in buildingsVar:
        if i[2] > vertical:
            vertical = i[2]

        if i[1] > orizontal:
            orizontal = i[1]
            
    for i in range(vertical + 2):
        acumulation.append([])
        for j in range(orizontal + 2):
            acumulation[-1].append(0)
    
    for i in buildingsVar:
        populateWithOnes(i, acumulation)

    for i in range(len(acumulation)):
        for j in range(len(acumulation[i])):
            if acumulation[i][j] == 1 and acumulation[i - 1][j] == 1 and acumulation[i + 1][j] == 0 and acumulation[i][j - 1] == 0 and acumulation[i][j + 1] == 1:
                result.append([j,i + 1])

            if acumulation[i][j] == 1 and acumulation[i - 1][j] == 1 and acumulation[i + 1][j] == 1 and acumulation[i][j - 1] == 1 and acumulation[i][j + 1] == 1 and acumulation[i + 1][j + 1] == 0:
                result.append([j,i + 1])

            if acumulation[i][j] == 1 and acumulation[i][j - 1] == 1 and acumulation[i][j + 1] == 0 and acumulation[i + 1][j] == 1 and i == 0: 
                result.append([j,i])
    
    return result
            
buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]],[[0,2,3],[2,5,3]]

for test in range(len(buildings)):
    print(colored(f"Test {(test + 1)}:","green"), getSkyline(buildings[test]), "|", colored("Passed","green"))