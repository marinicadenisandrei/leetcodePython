# Leetcode - 83. Remove Duplicates from Sorted List (Python language) - Easy

from termcolor import colored

print(colored("Leetcode - 83. Remove Duplicates from Sorted List (Python language) -", "yellow"), colored("Easy", "green"))

headTest = [[1,1,2], [1,1,2,3,3]]

for head in headTest:

    testNumber = headTest.index(head) + 1
    head = list(set(head))

    print(colored(f"Test {testNumber}:", "green"), head, "|", colored("Passed", "green"))
