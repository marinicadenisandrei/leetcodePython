# Leetcode - 230. Kth Smallest Element in a BST (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 230. Kth Smallest Element in a BST (Python language) - Medium","yellow"))

def kthSmallest(rootVar, kVar):
    rootVar.sort()
    rootVar = [i for i in rootVar if i != 0]
    return rootVar[kVar - 1]

root = [[3,1,4,0,2],[5,3,6,2,4,0,0,1]]
k = [1,3]

for test in range(len(k)):    
    print(colored(f"Test {(test + 1)}:","green"),kthSmallest(root[test], k[test]),"|",colored("Passed","green"))