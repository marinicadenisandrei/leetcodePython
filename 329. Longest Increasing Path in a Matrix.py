# Leetcode - 329. Longest Increasing Path in a Matrix (Python language) - Hard

from termcolor import colored

print(colored("Leetcode - 329. Longest Increasing Path in a Matrix (Python language) -","yellow"), colored("Hard","red"))

def LongestIncreasingPath(matrixVar):
    acumulation = []

    for i in range(len(matrixVar)):
        for j in range(len(matrixVar[i])):
            index_i = i
            index_j = j

            element = matrixVar[index_i][index_j]

            flag = True
            counter = 1

            while flag:
                flag = False

                if index_i + 1 < len(matrixVar) and matrixVar[index_i + 1][index_j] > element and matrixVar[index_i + 1][index_j] != element:
                    index_i += 1
                    flag = True
                elif index_j + 1 < len(matrixVar[index_i]) and matrixVar[index_i][index_j + 1] > element and matrixVar[index_i][index_j + 1] != element:
                    index_j += 1
                    flag = True
                elif index_j - 1 >= 0 and matrixVar[index_i][index_j - 1] > element:
                    index_j -= 1
                    flag = True
                elif index_i - 1 >= 0 and matrixVar[index_i - 1][index_j] > element:
                    index_i -= 1
                    flag = True
                else:
                    flag = False
                    break
                
                element = matrixVar[index_i][index_j]
                counter += 1

            acumulation.append(counter)
    
    return max(acumulation)
            
matrix = [[[9,9,4],[6,6,8],[2,1,1]],[[3,4,5],[3,2,6],[2,2,1]]]

for test in range(len(matrix)):
    print(colored(f"Test {(test + 1)}:","green"), LongestIncreasingPath(matrix[test]), "|", colored("Passed","green"))

    