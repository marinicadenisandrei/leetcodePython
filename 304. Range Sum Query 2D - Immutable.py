# Leetcode - 304. Range Sum Query 2D - Immutable (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 304. Range Sum Query 2D - Immutable (Python language) - Medium","yellow"))

class NumMatrix:
    def __init__(self, matrix):
        self.matrix = matrix
    
    def sumRegion(self, row1, col1, row2, col2):
        totalSum = 0

        for i in range(row1, row2 + 1):
            totalSum += sum(self.matrix[i][col1:col2 + 1])
        
        return totalSum
            

numMatrix = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
print(colored("Test 1:", "green"), numMatrix.sumRegion(2, 1, 4, 3), numMatrix.sumRegion(1, 1, 2, 2), numMatrix.sumRegion(1, 2, 2, 4), "|", colored("Passed","green"))