# Leetcode - 319. Bulb Switcher (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 319. Bulb Switcher (Python language) - Medium","yellow"))

def BulbSwitch(nVar):
    bulb = [1] * nVar

    for i in range(2, nVar + 1):
        for j in range(i - 1, len(bulb), i):
            if bulb[j] == 0:
                bulb[j] = 1
            else:
                bulb[j] = 0
        
    return bulb.count(1)
            
n = [3,0,1]

for test in range(len(n)):
    print(colored(f"Test {(test + 1)}:","green"), BulbSwitch(n[test]), "|", colored("Passed","green"))