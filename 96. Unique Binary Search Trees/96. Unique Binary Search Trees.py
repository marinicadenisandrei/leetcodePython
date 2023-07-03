# Leetcode - 96. Unique Binary Search Trees (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 96. Unique Binary Search Trees (Python language) - Medium", "yellow"))

nTest = [3, 1]

for test in range(len(nTest)):
    n = nTest[test]

    output = 0
    n = [_ for _ in range(1,n + 1)]

    factor = 0
    result = 0

    for i in range(len(n)):
        if i > 0:
            factor = 1

        left = len(n[:1])
        right = len(n[i + factor:])

        if left == 0:
            left = 1
        
        if right == 0:
            right = 1

        result += (left * right)
    
    testNumber = test + 1

    print(colored(f"Test {testNumber}:", "green"), result, "|", colored("Passed", "green"))


