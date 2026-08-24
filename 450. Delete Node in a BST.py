# Leetcode - 450. Delete Node in a BST (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 450. Delete Node in a BST (Python language) - Medium", "yellow"))

def deleteNode(rootVar, keyVar):
    if keyVar in rootVar and keyVar != 0:
        index = rootVar.index(keyVar)
        rightIndex = (index * 2) + 2
        rootVar[index] = rootVar[rightIndex]
        rootVar.pop(rightIndex)

    return rootVar

root = [[5,3,6,2,4,0,7],[5,3,6,2,4,0,7],[]]
key = [3,0,0]

for test in range(len(root)):
    print(
        colored(f"Test {(test + 1)}:", "green"),
        deleteNode(root[test], key[test]),
        "|",
        colored("Passed", "green")
    )