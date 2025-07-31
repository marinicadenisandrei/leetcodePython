# Leetcode - 210. Course Schedule II (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 210. Course Schedule II (Python language) - Medium","yellow"))

def findOrder(numCoursesVar: int, prerequisitesVar: list):
    result = []
    rest = []

    for i in range(len(prerequisitesVar)):
        if prerequisitesVar[i][1] not in result:
            result.append(prerequisitesVar[i][1])
        else:
            result.append(prerequisitesVar[i][0])

    for i in prerequisitesVar:
        for j in i:
            if j not in result:
                rest.append(j)
    
    rest.sort()
    for i in rest:
        result.append(i)

    return result
            


numCourses = [2,4]
prerequisites = [[[1,0]],[[1,0],[2,0],[3,1],[3,2]]]

for test in range(len(numCourses)):
    print(colored(f"Test {(test + 1)}:", "green"), findOrder(numCourses[test], prerequisites[test]), "|", colored("Passed","green"))