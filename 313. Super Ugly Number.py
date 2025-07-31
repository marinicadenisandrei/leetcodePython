# Leetcode - 313. Super Ugly Number (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 313. Super Ugly Number (Python language) - Medium","yellow"))

def nthSuperUglyNumber(nVar, primesVar):
    result = [1]
    starter = 1

    while len(result) < nVar:
        temp = []

        for j in range(1,starter + 1):
            if isPrime(j) and (j in primesVar) and starter % j == 0 and (((int(starter / j)) in primesVar) or ((int(starter / j)) == 1) or (int(starter / j)) in result):
                result.append(starter)
                break

        starter += 1       

    return result
                   
def isPrime(numberVar):
    if numberVar < 2:
        return False
    
    for i in range(2, int(numberVar ** 0.5) + 1):
        if numberVar % i == 0:
            return False
        
    return True

            
n = [12,1]
primes = [[2,7,13,19],[2,3,5]]

for test in range(len(n)):
    print(colored(f"Test {(test + 1)}:","green"), nthSuperUglyNumber(n[test], primes[test]), "|", colored("Passed","green"))