# Leetcode - 107. Binary Tree Level Order Traversal II (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 107. Binary Tree Level Order Traversal II (Python language) - Medium", "yellow"))

rootTest = [[3,9,20,0,0,15,7], [1], []]

for test in range(len(rootTest)):
    root = rootTest[test]
    output = []
    counter = 0

    while len(root) > 0:
        if 0 in root[:pow(2,counter)]:
            temp = [_ for _ in root[:pow(2,counter)] if _ != 0]
            output.append(temp)
        else:
            output.append(root[:pow(2,counter)])

        root = root[pow(2,counter):]
        counter += 1

    output.reverse()

    testNumber = test + 1
    print(colored(f"Test {testNumber}:", "green"), output, "|", colored("Passed", "green"))