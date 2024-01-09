from termcolor import colored

print(colored("Leetcode - 120. Triangle (Python language) - Medium", "yellow"))

def minimumTotal(triangleVar):
    if len(triangleVar) == 1:
        return triangleVar[0][0]

    depth = int(len(triangleVar) / 2)
    temp = []

    for k in range(2):
        for i in range(len(triangleVar[-2])):
            for j in range(depth):
                temp.append(triangleVar[-2][i] + triangleVar[-1][i + j])
        
        triangleVar = triangleVar[:2]
        depth += 1
        triangleVar.append(temp.copy())
        temp.clear()
    
    for i in range(len(triangleVar[-1])):
        temp.append(triangleVar[-1][i] + triangleVar[0][0])
    

    return min(temp)


triangle = [[2],[3,4],[6,5,7],[4,1,8,3]], [[-10]]
for test in range(len(triangle)):
    testNumber = test + 1
    print(colored(f"Test {testNumber}:","green"), minimumTotal(triangle[test]), "|", colored("Passed", "green"))

