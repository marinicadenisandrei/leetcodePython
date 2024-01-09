# Leetcode - 111. Minimum Depth of Binary Tree (Python language) - Easy

from termcolor import colored

print(colored("Leetcode - 111. Minimum Depth of Binary Tree (Python language) -", "yellow"), colored("Easy", "green"))

root = [[3,9,20,0,0,15,7], [2,0,3,0,4,0,5,0,6]]

def minDepth(rootVar):
    rootVar = rootVar[1:]
    power = 2

    depth = 0
    flag = False
    counter = 1

    for i in range(3):
        top = rootVar[:pow(2,power - 1)].copy()
        rootVar = rootVar[pow(2,power - 1):]
        bottom = rootVar[:pow(2,power)].copy()

        if flag:
            temp = []
            temp.extend(top[-2:])
            temp.extend(bottom.copy())
            bottom = temp.copy()
            temp = []
            flag = False

        if len(top) == 0 or len(bottom) == 0:
            break

        power += 1
    
        for j in range(len(top)):
            if top[j] == 0:
                flag = True
                continue
            else:
                counter += 1

        top = []
        bottom = []
    
    return counter

for test in range(len(root)):
    testNumber = test + 1
    print(colored(f"Test {testNumber}:", "green"), minDepth(root[test]), "|", colored("Passed", "green"))
