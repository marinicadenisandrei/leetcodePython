# Leetcode - 142. Linked List Cycle II (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 142. Linked List Cycle II (Python language) - Medium", "yellow"))

def detectCycle(headVar : list, pos : int):
    if headVar.index(headVar[-1]) > pos:
        return f"tail connects to node index {pos}"
    
    return "tail connects to node index -1"
        
head = [[3,2,0,-4], [1,2]]
pos = [1, 0]

for test in range(len(head)):
    print(colored(f"Test {(test + 1)}:", "green"), detectCycle(head[test], pos[test]), "|",colored("Passed", "green"))