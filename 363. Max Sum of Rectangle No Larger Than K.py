# Leetcode - 363. Max Sum of Rectangle No Larger Than K (Python language) - Hard

from termcolor import colored

print(colored("Leetcode - 363. Max Sum of Rectangle No Larger Than K (Python language) -", "yellow"), colored("Hard","red"))

def maxSumSubmatrix(matrixVar, kVar):
    result = float('-inf')

    for i in range(len(matrixVar)):
        for j in range(len(matrixVar[i])):
            for k in range(i, len(matrixVar)):
                for l in range(j, len(matrixVar[k])):
                    tempSum = 0
                    for x in range(i, k + 1):
                        for y in range(j, l + 1):
                            tempSum += matrixVar[x][y]
                    
                    if result < tempSum and tempSum <= kVar:
                        result = tempSum
    
    return result

matrix = [[[1,0,1],[0,-2,3]],[[2,2,-1]]]
k = [2,3]

for test in range(len(k)):
    print(colored(f"Test {(test + 1)}:", "green"), maxSumSubmatrix(matrix[test], k[test]), "|", colored("Passed","green"))

