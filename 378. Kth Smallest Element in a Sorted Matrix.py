# Leetcode - 378. Kth Smallest Element in a Sorted Matrix (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 378. Kth Smallest Element in a Sorted Matrix (Python language) - Medium","yellow"))

def kthSmallest(matrixVar, kVar):
    return [x for row in matrixVar for x in row][kVar - 1]
    
matrix = [[[1,5,9],[10,11,13],[12,13,15]],[[-5]]] 
k = [8,1]

for test in range(len(matrix)):
    print(colored(f"Test {(test + 1)}:","green"), kthSmallest(matrix[test], k[test]), "|", colored("Passed","green"))