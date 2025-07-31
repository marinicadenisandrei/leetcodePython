# Leetcode - 82. Remove Duplicates from Sorted List II (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 82. Remove Duplicates from Sorted List II (Python language) - Medium", "yellow"))

headTest = [[1,2,3,3,4,4,5], [1,1,1,2,3]]

for head in headTest:
    testNumber = headTest.index(head) + 1
    head = list(filter(lambda x: head.count(x) == 1, head))
    
    print(colored(f"Test {testNumber}:", "green"), head, "|", colored("Passed", "green"))
