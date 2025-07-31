# Leetcode - 141. Linked List Cycle (Python language) - Easy

from termcolor import colored

print(colored("Leetcode - 141. Linked List Cycle (Python language) -", "yellow"), colored("Easy", "green"))

def hasCycle(headVar : list, posVar : int):
    if posVar <= len(headVar) and posVar >= 0:
        return True

    return False

head = [[3,2,0,-4], [1,2], [1]]
pos = [1,0,-1]

for test in range(len(pos)):
    print(colored(f"Test {(test + 1)}:", "green"), hasCycle(head[test], pos[test]), "|", colored("Passed", "green"))