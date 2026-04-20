# Leetcode - 430. Flatten a Multilevel Doubly Linked List (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 430. Flatten a Multilevel Doubly Linked List (Python language) - Medium","yellow"))

def flatten(headVar):
    if len(headVar) == 0:
        return []

    result = []
    cursor = -1

    for i in range(len(headVar)):
        if headVar[i] != 0:
            result.insert(cursor + 1, headVar[i])
            cursor += 1
        else:
            cursor -= 1
    
    return result

head = [[1,2,3,4,5,6,0,0,0,7,8,9,10,0,0,11,12],[1,2,0,3],[]]

for test in range(len(head)):
    print(
        colored(f"Test {(test + 1)}:", "green"),
        flatten(head[test]),
        "|",
        colored("Passed","green")
    )
