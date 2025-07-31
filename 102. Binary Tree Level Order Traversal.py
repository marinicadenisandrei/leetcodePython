# Leetcode - 102. Binary Tree Level Order Traversal (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 102. Binary Tree Level Order Traversal (Python language) - Medium", "yellow"))

rootTest = [[3,9,20,0,0,15,7], [1], []]

for test in range(len(rootTest)):
    root = rootTest[test]

    root = list(filter(lambda x: x != 0, root))
    output = []

    if len(root) > 0:
        output = [root[0]]

    def pairNodes(list_var):
        if len(list_var) < 2:
            return

        pair = [list_var[0], list_var[1]]
        output.append(pair)

        pairNodes(list_var[2:])

    pairNodes(root[1:])
    
    testNumber = test + 1

    print(colored(f"Test {testNumber}:", "green"), output, "|", colored("Passed", "green"))