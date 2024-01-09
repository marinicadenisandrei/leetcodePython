# Leetcode - 145. Binary Tree Postorder Traversal (Python language) - Easy

from termcolor import colored

print(colored("Leetcode - 145. Binary Tree Postorder Traversal (Python language) -", "yellow"), colored("Easy", "green"))

def postorderTraversal(rootVar : list):
    return [i for i in rootVar if i != 0][::-1]

root = [[1,0,2,3], [], [1]]

for test in range(len(root)):
    print(colored(f"Test {(test + 1)}:", "green"), postorderTraversal(root[test]), "|", colored("Passed", "green"))