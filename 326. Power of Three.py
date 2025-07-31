# Leetcode - 326. Power of Three (Python language) - Easy

from termcolor import colored

print(colored("Leetcode - 326. Power of Three (Python language) -","yellow"), colored("Easy","green"))

def IsPowerOfThree(nVar):
    for i in range(2, int(nVar / 2)):
        copyOfnVar = nVar

        while copyOfnVar > 1:
            copyOfnVar /= i

        if copyOfnVar == 1.0:
            return True
    
    return False
        
n = [27,0,-1]

for test in range(len(n)):
    print(colored(f"Test {(test + 1)}:","green"), IsPowerOfThree(n[test]), "|", colored("Passed","green"))
    