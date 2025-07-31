# Leetcode - 202. Happy Number (Python language) - Easy

from termcolor import colored

print(colored("Leetcode - 202. Happy Number (Python language) -","yellow"), colored("Easy","green"))

def isHappy(nVar: int):
    nVarStr = str(nVar)
    powSum = 0

    while len(nVarStr) > 1:
        for i in nVarStr:
            powSum += pow(int(i),2)
    
        nVarStr = str(powSum)
        powSum = 0

    if nVarStr == "1":
        return True
        
    return False
        
n = [19,2]

for test in range(len(n)):
    print(colored(f"Test {(test + 1)}:","green"), isHappy(n[test]), "|", colored("Passed","green"))