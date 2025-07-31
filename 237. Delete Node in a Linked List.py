# Leetcode - 237. Delete Node in a Linked List (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 237. Delete Node in a Linked List (Python language) - Medium","yellow"))

def deleteNode(headVar, nodeVar):
    headVar.remove(nodeVar)

head = [[4,5,1,9],[4,5,1,9]]
node = [5,1]

for test in range(len(head)):
    deleteNode(head[test], node[test])
    print(colored(f"Test {(test + 1)}:","green"), head[test], "|", colored("Passed","green"))