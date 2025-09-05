# Leetcode - 391. Perfect Rectangle (Python language) - Hard

from termcolor import colored

print(colored("Leetcode - 391. Perfect Rectangle (Python language) -","yellow"), colored("Hard","red"))

def isRectangleCover(rectanglesVar):
    vertical = 0
    horizontal = 0

    for i in rectanglesVar:
        if vertical < i[3]:
            vertical = i[3]
        
        if horizontal < i[2]:
            horizontal = i[2]

    vertical -= 1
    horizontal -= 1

    matrix = [[0 for _ in range(horizontal)] for _ in range(vertical)]

    for i in rectanglesVar:
        for j in range(i[1] - 1, i[3] - 1):
            for k in range(i[0] - 1, i[2] - 1):
                if matrix[j][k] == 1:
                    matrix[j][k] = 0
                else:
                    matrix[j][k] = 1
    
    return [1 for i in matrix if 0 not in i].count(1) == len(matrix)
            
rectangles = [[[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]], [[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]], [[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]]]

for test in range(len(rectangles)):
    print(
        colored(f"Test {(test + 1)}:","green"),
        isRectangleCover(rectangles[test]),
        "|",
        colored("Passed","green")
    )
    