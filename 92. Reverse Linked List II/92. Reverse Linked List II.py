# Leetcode - 92. Reverse Linked List II (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 92. Reverse Linked List II (Python language) - Medium", "yellow"))

headTest = [[1, 2, 3, 4, 5], [5]]

leftTest = [2, 1]
rightTest = [4, 1]

for test in range(len(headTest)):
    head = headTest[test]
    left = leftTest[test]
    right = rightTest[test]

    if left in head and right in head:
        left = head.index(left)
        right = head.index(right)
        
        head[left], head[right] = head[right], head[left]


    testNumber = test + 1

    print(colored(f"Test {testNumber}:", "green"), head, "|", colored("Passed", "green"))
