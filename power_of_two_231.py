# Leetcode - 231. Power of Two (Python language) - Easy

from termcolor import colored
print(colored("Leetcode - 231. Power of Two (Python language) -","yellow"), colored("Easy","green"))

def isPowerOfTwo(nVar):
    for i in range(nVar):
        if pow(2,i) == nVar:
            return True
            
    return False
        
n = [1,16,3]
for test in range(len(n)):
    print(colored(f"Test {(test + 1)}:","green"), isPowerOfTwo(n[test]), "|", colored("Passed","green"))