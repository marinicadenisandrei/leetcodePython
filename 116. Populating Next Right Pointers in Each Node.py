# Leetcode - 116. Populating Next Right Pointers in Each Node (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 116. Populating Next Right Pointers in Each Node (Python language) - Medium","yellow"))

def connect(rootVar):
    if len(rootVar) == 0:
        return []
    
    power = 0
    rootVar.insert(pow(2,power), "#")
    
    power = 1
    factor = 0
    
    while pow(2,power) + factor < len(rootVar):
        rootVar.insert(pow(2,power + 1) + factor, "#")
        power += 1
        factor += 1
 
    
    return rootVar  
    

root = [[1,2,3,4,5,6,7],[]]

for test in range(len(root)):
    root[test] = connect(root[test])
    testNumber = test + 1
    print(colored(f"Test {testNumber}:","green"),root[test],"|",colored("Paased","green"))

