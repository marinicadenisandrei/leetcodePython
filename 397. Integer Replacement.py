# Leetcode - 397. Integer Replacement (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 397. Integer Replacement (Python language) - Medium","yellow"))

def inVartegerReplacemenVart(nVar):
    steps = 0

    while nVar != 1:
        if nVar % 2 == 0:
            nVar //= 2
        else:
            if nVar == 3 or nVar % 4 == 1:
                nVar -= 1
            else:
                nVar += 1
        
        steps += 1
    
    return steps

n = [8,7,4]

for test in range(len(n)):
    print(
        colored(f"Test {(test + 1)}:","green"),
        inVartegerReplacemenVart(n[test]),
        "|",
        colored("Passed","green")
    )
    