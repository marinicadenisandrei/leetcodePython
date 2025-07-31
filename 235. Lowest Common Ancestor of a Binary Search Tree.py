# Leetcode - 235. Lowest Common Ancestor of a Binary Search Tree (Python language) - Medium

from termcolor import colored
print(colored("Leetcode - 235. Lowest Common Ancestor of a Binary Search Tree (Python language) - Medium","yellow"))

def lowestCommonAncestor(rootVar, pVar, qVar):
    for i in range(len(rootVar)):
        if (i * 2) + 2 > len(rootVar):
            break

        try:
            node = [rootVar[i], rootVar[(i * 2) + 1], rootVar[(i * 2) + 2]]
        except IndexError:
            return rootVar[0]

        if pVar in node and qVar in node:
            return node[0]
    
root = [[6,2,8,0,4,7,9,0,0,3,5],[6,2,8,0,4,7,9,0,0,3,5],[2,1]]
p = [2,2,2] 
q = [8,4,1]

for test in range(len(p)):
    print(colored(f"Test {(test + 1)}:","green"), lowestCommonAncestor(root[test], p[test], q[test]), "|", colored("Passed","green"))

