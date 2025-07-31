from termcolor import colored

print(colored("Leetcode - 144. Binary Tree Preorder Traversal (Python language) -", "yellow"), colored("Passed", "green"))

def preorderTraversal(rootVar : list):
    if 0 in rootVar:
        return [i for i in rootVar if i != 0]
    else:
        return rootVar
        

root = [[1,0,2,3], [], [1]]

for test in range(len(root)):
    print(colored(f"Test {(test + 1)}:", "green"), preorderTraversal(root[test]), "|", colored("Passed", "green"))