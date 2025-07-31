# Leetcode - 372. Super Pow (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 372. Super Pow (Python language) - Medium","yellow"))

def superPow(aVar, bVar):
    return aVar**int("".join(str(_) for _ in bVar))
    
a = [2,2,1]
b = [[3],[1,0],[4,3,3,8,5,2]]

for test in range(len(a)):
    print(colored(f"Test {(test + 1)}:", "green"), superPow(a[test], b[test]), "|", colored("Passed","green"))