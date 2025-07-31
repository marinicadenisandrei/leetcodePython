# Leetcode - 263. Ugly Number (Python language) - Easy 

from termcolor import colored

print(colored("Leetcode - 263. Ugly Number (Python language) -", "yellow"), colored("Easy","green"))

def isUgly(nVar):
    while nVar > 1:
        if nVar % 2 == 0:
            nVar = int(nVar / 2)
        elif nVar % 3 == 0:
            nVar = int(nVar / 3)
        elif nVar % 5 == 0:
            nVar = int(nVar / 5)
        else:
            return False
            
    return True
        
n = [6,1,14]

for test in range(len(n)):
    print(colored(f"Test {(test + 1)}:", "green"), isUgly(n[test]), "|", colored("Passed","green"))