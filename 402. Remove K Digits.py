# Leetcode - 402. Remove K Digits (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 402. Remove K Digits (Python language) - Medium", "yellow"))

def removeKdigits(numsVar, kVar):       
    for i in range(kVar):
        for j in range(len(numsVar) - 1):
            if numsVar[j] < numsVar[j + 1]:
                numsVar = numsVar[:j + 1] + numsVar[j + 2:]
                break
            else:
                numsVar = numsVar[:j] + numsVar[j + 1:]
                break
        
    return str(int(numsVar))
    
num = ["1432219","10200","10"]
k = [3,1,2]

for test in range(len(num)):
    print(
        colored(colored(f"Test {(test + 1)}:", "green")),
        removeKdigits(num[test], k[test]),
        "|",
        colored("Passed","green")
    )