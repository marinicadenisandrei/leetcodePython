# Leetcode - 386. Lexicographical Numbers (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 386. Lexicographical Numbers (Python language) - Medium","yellow"))

def lexicalOrder(nVar):
    result = [str(i) for i in range(1, nVar)]
    result.sort()
    
    return [int(i) for i in result]

n = [13,2]

for test in range(len(n)):
    print(
        colored(f"Test {(test + 1)}:", "green"),
        lexicalOrder(n[test]),
        "|",
        colored("Passed","green")
    )
    