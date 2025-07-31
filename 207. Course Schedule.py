# Leetcode - 207. Course Schedule (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 207. Course Schedule (Python language) - Medium","yellow"))

def canFinish(numCoursesVar: int , prerequisitesVar: list):
    for i in prerequisitesVar:
        for j in range(len(i) - 1):
            if i[j] < i[j + 1]:
                return False
    
    return True
            
numCourses = [2,2] 
prerequisites = [[[1,0]],[[1,0],[0,1]]]

for test in range(len(prerequisites)):
    print(colored(f"Test {(test + 1)}:", "green"), canFinish(numCourses[test], prerequisites[test]), "|", colored("Passed","green"))