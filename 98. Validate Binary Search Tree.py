# Leetcode - 98. Validate Binary Search Tree (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 98. Validate Binary Search Tree (Python language) - Medium", "yellow"))

rootTest = [[2,1,3], [5,1,4,0,0,3,6]]
BTS = [[].copy()] * 3

def rightBST(parent, left, right):
    if parent > left and parent < right:
        return True
    else:
        return False

def depth(length):
    power = 0
    counter = 0

    while length > 0:
        power = pow(2,counter)
        length -= power

        counter += 1
    
    return power - 1


for test in range(len(rootTest)):
    root = rootTest[test]
    flag = True
    
    for parent in range(1, depth(len(root)) + 1):
        if rightBST(root[parent - 1], (root[(parent * 2) - 1]), ((root[parent * 2]))) == False:
            flag = False
            break

    testNumber = test + 1

    print(colored(f"Test {testNumber}:", "green"), flag, "|", colored("Passed", "green"))

