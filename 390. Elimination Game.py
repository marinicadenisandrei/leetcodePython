# Leetcode - 390. Elimination Game (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 390. Elimination Game (Python language) - Medium","yellow"))

def lastRemaining(nVar):
    starterList = [i for i in range(1, nVar + 1)]
    switch = 1
    
    while len(starterList) > 1:
        temp = [starterList[i] for i in range(switch, len(starterList), 2)]
        
        if switch == 1: 
            switch = 0 
        else: 
            switch = 1 
        
        starterList = temp.copy()
        
    return starterList[0]
    
n = [9,1]

for test in range(len(n)):
    print(
        colored(f"Test {(test + 1)}:","green"),
        lastRemaining(n[test]),
        "|",
        colored("Passed","green")
    )
    