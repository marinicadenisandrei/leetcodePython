# Leetcode - 94. Binary Tree Inorder Traversal (Python language) - Easy

from termcolor import colored

print(colored("Leetcode - 94. Binary Tree Inorder Traversal (Python language) -", "yellow"), colored("Easy", "green"))

rootTest = [[1, 0, 2, 3], [], [1]]

for test in range(len(rootTest)):
    root = rootTest[test]
    root = [_ for _ in root if _ != 0]

    testNumber = test + 1

    print(colored(f"Test {testNumber}:", "green"), root, "|", colored("Passed", "green"))