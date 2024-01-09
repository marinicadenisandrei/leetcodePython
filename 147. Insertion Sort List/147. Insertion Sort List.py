# Leetcode - 147. Insertion Sort List (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 147. Insertion Sort List (Python language) - Medium", "yellow"))

def insertionSortList(headVar: list):
    flag = True

    while flag:
        flag = False
        for i in range(1,len(headVar)):
            if headVar[i - 1] > headVar[i]:
                headVar[i - 1], headVar[i] = headVar[i], headVar[i - 1]
                flag = True
                break
    
    return headVar

head = [[4,2,1,3], [-1,5,3,4,0]]

for test in range(len(head)):
    head[test] = insertionSortList(head[test])
    print(colored(f"Test {(test + 1)}:", "green"), head[test], "|", colored("Passed", "green"))

