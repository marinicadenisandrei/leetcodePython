# Leetcode - 74. Search a 2D Matrix (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 74. Search a 2D Matrix (Python language) - Medium", "yellow"))

matrixTest = [[[1,3,5,7],[10,11,16,20],[23,30,34,60]], [[1,3,5,7],[10,11,16,20],[23,30,34,60]]]
targetTest = [3, 13]

for test in range(len(matrixTest)):
    matrix = matrixTest[test]
    target = targetTest[test]

    flag = False

    for i in matrix:
        if target in i:
            flag = True

    testNumber = test + 1
    
    print(colored(f"Test {testNumber}:", "green"), flag, "|", colored("Passed", "green"))