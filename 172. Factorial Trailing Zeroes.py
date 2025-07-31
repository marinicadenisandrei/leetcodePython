# Leetcode - 172. Factorial Trailing Zeroes (Python language) - Medium

from termcolor import colored
print(colored("Leetcode - 172. Factorial Trailing Zeroes (Python language) - Medium","yellow"))

def trailingZeroes(nVar):
    factorial = 1
    for i in range(1,nVar + 1): factorial *= i
    
    return str(factorial).count("0")
        

n = [3,5,0]

for test in range(len(n)):
    print(colored(f"Test {(test + 1)}:","green") ,trailingZeroes(n[test]), "|", colored("Passed","green"))