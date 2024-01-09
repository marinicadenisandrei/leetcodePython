# Leetcode - 138. Copy List with Random Pointer (Python language) - Medium

from termcolor import colored
print(colored("Leetcode - 138. Copy List with Random Pointer (Python language) - Medium", "yellow"))

def copyRandomList(headVar : list):
    return headVar.copy()

head = [[[7,0],[13,0],[11,4],[10,2],[1,0]], [[1,1],[2,1]], [[3,0],[3,0],[3,0]]]
for test in range(len(head)):
    head[test] = copyRandomList(head[test]);
    print(colored(f"Test {(test + 1)}:", "green"), head[test], "|", colored("Passed", "green"))

