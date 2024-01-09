# Leetcode - 110. Balanced Binary Tree (Python language) - Easy

from termcolor import colored

print(colored("Leetcode - 110. Balanced Binary Tree (Python language) -", "yellow"), colored("Easy", "green"))

def depthBin(listVar):
    lenVar = len(listVar)
    power = 0

    while lenVar > 1:
        lenVar -= pow(2,power)
        power += 1
    
    if lenVar < 0:
        lenVar = abs(lenVar)

        for i in range(lenVar):
            listVar.append(0)

    return power

rootTest = [[3,9,20,0,0,15,7], [1,2,2,3,3,0,0,4,4],[]]

for test in range(len(rootTest)):
    root = rootTest[test]

    flag = True
    power = 1
    index1 = 0
    index2 = 1

    counter = 0

    node = root[index1:index2].copy()
    members = root[index1 + 1:index2 + 2].copy()

    while len(node) > 0:
        if 0 in [node[0], members[0], members[1]]:
                counter += 1
    
        node = node[1:]
        members = members[2:]

    for i in range(depthBin(root) - 1):
        index1 = pow(2,power) - 1
        index2 = pow(2,power + 1) - 1
        index3 = pow(2,power + 2) - 1

        node = root[index1:index2].copy()
        members = root[index2:index3].copy()

        while len(node) > 0:
            try:
                if 0 in [node[0], members[0], members[1]]:
                    counter += 1
            except IndexError:
                break

            node = node[1:]
            members = members[2:]

        power += 1

    if counter > 1:
        flag = False
    
    testNumber = test + 1
    
    print(colored(f"Test {testNumber}:", "green"), flag, "|", colored("Passed", "green"))


    

