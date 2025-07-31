# Leetcode - 203. Remove Linked List Elements (Python language) - Easy

from termcolor import colored

print(colored("Leetcode - 203. Remove Linked List Elements (Python language) -","yellow"),colored("Easy","green"))

def removeElements(headVar: list, valVar: int):
    headVar = list(filter(lambda x: x != valVar, headVar))
    return headVar

head = [[1,2,6,3,4,5,6],[],[7,7,7,7]]
val = [6,1,7]

for test in range(len(head)):
    print(colored(f"Test {(test + 1)}:", "green"), removeElements(head[test], val[test]), "|", colored("Passed","green"))