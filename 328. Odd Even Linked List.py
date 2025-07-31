# Leetcode - 328. Odd Even Linked List (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 328. Odd Even Linked List (Python language) - Medium","yellow"))

def OddEvenList(headVar):
    acumulation = []

    for i in range(1, len(headVar), 2):
        acumulation.append(headVar[i])
        
    headVar = [i for i in headVar if i not in acumulation]
    headVar.extend(acumulation)

    return headVar

head = [[1,2,3,4,5],[2,1,3,5,6,4,7]]

for test in range(len(head)):
    print(colored(f"Test {(test + 1)}:","green"), OddEvenList(head[test]),"|",colored("Passed","green"))
    