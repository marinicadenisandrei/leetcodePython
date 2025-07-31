# Leetcode - 109. Convert Sorted List to Binary Search Tree (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 109. Convert Sorted List to Binary Search Tree (Python language) - Medium", "yellow"))

headTest = [[-10,-3,0,5,9], []]

for test in range(len(headTest)):
    head = headTest[test]
    output = []

    if len(head) > 2:
        mid = int(len(head)/2)

        left = head[:mid][::-1]
        right = head[mid + 1:][::-1]

        output = [head[mid], left[0], right[0]]

        for i,j in zip(left[1:], right[1:]):
            output.append(i)
            output.append(0)
            output.append(j)
            output.append(0)

    
    testNumber = test + 1

    print(colored(f"Test {testNumber}:", "green"), output, "|", colored("Passed", "green"))

