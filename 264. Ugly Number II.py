# Leetcode - 264. Ugly Number II (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 264. Ugly Number II (Python language) - Medium", "yellow"))

def isUgly(nVar):
    if nVar == 1:
        return 1
        
    counter = 0 
    flag = True
    
    number = 1

    while flag:
        good = True
        history = number

        while number > 1:
            if number % 2 == 0:
                number = int(number / 2)
            elif number % 3 == 0:
                number = int(number / 3)
            elif number % 5 == 0:
                number = int(number / 5)
            else:
                good = False
                break
        
        number = history

        if good:
            counter += 1

        if counter == nVar:
            return number

        number += 1
            
            
            
        
n = [10,1]

for test in range(len(n)):
    print(colored(f"Test {(test + 1)}:", "green"), isUgly(n[test]), "|", colored("Passed","green"))