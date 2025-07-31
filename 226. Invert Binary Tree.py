# Leetcode - 226. Invert Binary Tree (Python language) - Easy

from termcolor import colored

print(colored("Leetcode - 226. Invert Binary Tree (Python language) -","yellow"), colored("Easy","green"))

def invertTree(rootVar: list):
    formation = []

    if len(rootVar) == 0:
        return formation
    
    formation.append(rootVar[0])
    index1 = 1
    index2 = 2

    while index2 < len(rootVar):
        formation.extend(list(reversed(rootVar[index1:index2 + 1])))
        index1 = index2 + 1
        index2 = index1 * 2

    return formation

root = [[4,2,7,1,3,6,9],[2,1,3],[]]

for test in range(len(root)):
    print(colored(f"Test {(test + 1)}:","green"), invertTree(root[test]), "|", colored("Passed","green"))