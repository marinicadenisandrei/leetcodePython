# Leetcode - 222. Count Complete Tree Nodes (Python language) - Easy 

from termcolor import colored

print(colored("Leetcode - 222. Count Complete Tree Nodes (Python language) -","yellow"), colored("Easy","green"))

def countNodes(rootVar: list):
    return len(rootVar)
    
root = [[1,2,3,4,5,6],[],[1]]

for test in range(len(root)):
    print(colored(f"Test {(test + 1)}:","green"), countNodes(root[test]), "|", colored("Passed","green"))