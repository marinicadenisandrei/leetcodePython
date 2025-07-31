# Leetcode - 86. Partition List (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 86. Partition List (Python language) - Medium", "yellow"))

headTest = [[1,4,3,2,5,2], [2,1]]
xTest = [3, 2]

for test in range(len(headTest)):
    head = headTest[test]
    x = xTest[test]

    output = [i for i in head if i < x]
    output.extend([i for i in head if i >= x])

    testNumber = test + 1

    print(colored(f"Test {testNumber}:", "green"), output, "|", colored("Passed", "green"))