# Leetcode - 143. Reorder List (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 143. Reorder List (Python language) - Medium", "yellow"))

def reorderList(headVar : list):
    newList = []
    
    for i in range(int(len(headVar) / 2)):
        newList.append(headVar[i])
        newList.append(headVar[len(headVar) - i - 1])
        
    return newList

head = [[1,2,3,4], [1,2,3,4,5]]

for test in range(len(head)):
    head[test] = reorderList(head[test])
    print(colored(f"Test {(test + 1)}:", "green"), head[test], "|", colored("Passed"))
