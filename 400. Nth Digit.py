# Leetcode - 400. Nth Digit (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 400. Nth Digit (Python language) - Medium","yellow"))

def findNthDigit(nVar):
    return "".join([str(_) for _ in range(1, nVar + 1)])[nVar - 1]

n = [3,11]

for test in range(len(n)):
    print(
        colored(f"Test {test + 1}:","green"),
        findNthDigit(n[test]),
        "|",
        colored("Passed","green")
    )    
