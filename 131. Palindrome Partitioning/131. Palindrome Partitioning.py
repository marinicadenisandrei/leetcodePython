# Leetcode - 131. Palindrome Partitioning (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 131. Palindrome Partitioning (Python language) - Medium", "yellow"))

def isPal(sVar : str):
    if sVar == sVar[::-1]:
        return True
    
    return False

def partition(sVar : str):
    output = [[] for _ in range(3)]

    for i in range(len(sVar)):
        if isPal(sVar[i]):
            output[0].append(sVar[i])
        
        if isPal(sVar[:i]) and len(sVar[:i]) > 0:
            output[1].append(sVar[:i])

        if isPal(sVar[::-1][:i]) and len(sVar[::-1][:i]) > 0:
            output[2].append(sVar[::-1][:i])
        
    output = [_ for _ in output if len(_) > 0]
            
    return output

s = ["aab", "a"]

for test in range(len(s)):
    print(colored(f"Test {(test + 1)}:", "green"), partition(s[test]), "|", colored("Passed", "green"))