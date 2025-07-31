# Leetcode - 257. Binary Tree Paths (Python language) - Easy

from termcolor import colored
print(colored("Leetcode - 257. Binary Tree Paths (Python language) -", "yellow"), colored("Easy", "green"))

def binaryTreePaths(rootVar):
    indexList = []
    result = []
    start = 2
    levels = 0

    while start < len(rootVar):
        start *= 2
        levels += 1

    while len(rootVar) < start - 1:
        rootVar.append(0)
    
    indexVar = 0
    counter = 0
    divElement = int(start / 2)

    for i in range(levels + 1):
        indexList.append([])

        for j in range(int(start / 2)):
            if counter == divElement:
                indexVar += 1
                counter = 0

            indexList[-1].append(indexVar)

            counter += 1
                
        divElement /= 2
        divElement = int(divElement)
        counter = 0
        indexVar += 1

    for i in range(len(indexList[0])):
        temp = ""

        for j in range(len(indexList)):
            temp += str(rootVar[indexList[j][i]]) + "->"
        
        temp = temp[:-2]

        if temp not in result:
            result.append(temp)
            
    return result

root = [[1,2,3,0,5],[1]]

for test in range(len(root)):
    print(colored(f"Test {(test + 1)}:", "green"), binaryTreePaths(root[test]), "|", colored("Passed", "green"))