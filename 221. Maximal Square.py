# Leetcode - 221. Maximal Square (Pthon language) - Medium

from termcolor import colored
print(colored("Leetcode - 221. Maximal Square (Pthon language) - Medium","yellow"))

def maximalSquare(matrixVar: list):
    maxVar = 0

    for i in range(len(matrixVar)):
        for j in range(len(matrixVar[i])):
            if matrixVar[i][j] == "1":
                orizontal = 0
                vertical = 0
                
                for k in range(j, len(matrixVar[i])):
                    if matrixVar[i][k] == "1":
                        orizontal += 1
                    else:    
                        break

                for k in range(i, len(matrixVar)):
                    if matrixVar[k][j] == "1":
                        vertical += 1
                    else:
                        break
                
                if min(orizontal, vertical) > maxVar:
                    maxVar = min(orizontal, vertical)
    
    if maxVar > 1:
        return maxVar * 2

    return maxVar
                        
matrix = [[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]],[["0","1"],["1","0"]]]

for test in range(len(matrix)):
    print(colored(f"Test {(test + 1)}:","green"), maximalSquare(matrix[test]),"|",colored("Passed","green"))