# Leetcode - 204. Count Primes (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 204. Count Primes (Python language) - Medium","yellow"))

def countPrimes(nVar: int):
    counter = 0
    flag = True
    
    for i in range(2,nVar):
        flag = True
        
        for j in range(2,int(nVar / 2)):
            if j != 1 and i % j == 0 and i != j:
                flag = False
        
        if flag:
            counter += 1
    
    return counter
            
n = [10,0,1]

for test in range(len(n)):
    print(colored(f"Test {(test + 1)}:","green"), countPrimes(n[test]), "|", colored("Passed","green"))