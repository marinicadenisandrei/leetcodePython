# Leetcode - 240. Search a 2D Matrix II (Python language) - Medium

from termcolor import colored
print(colored("Leetcode - 240. Search a 2D Matrix II (Python language) - Medium","yellow"))

def searchMatrix(matrixVar, targetVar):
    for i in matrixVar:
        for j in i:
            if targetVar == j:
                return True
    
    return False

matrix = [[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]]
target = [5,20]

for test in range(len(matrix)):
    print(colored(f"Test {(test + 1)}:","green"), searchMatrix(matrix, target), "|", colored("Passed","green"))