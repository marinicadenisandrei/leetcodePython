# Leetcode - 132. Palindrome Partitioning II (Python language) - Hard

from termcolor import colored

print(colored("Leetcode - 132. Palindrome Partitioning II (Python language) -", "yellow"), colored("Hard", "red"))

def isPal(palVar : str):
    if palVar == palVar[::-1]:
        return True
    
    return False

def minCut(sVar : str):
    cuts = 0
    acumulation = []

    for i in range(len(sVar) + 1):
        if isPal(sVar[:i]) and isPal(sVar[:i + 1]):
            continue
        else:
            cuts += 1
    
    if cuts == 0:
        return 0
    
    return cuts - 1
    
s = ["aab", "a", "ab"]
for test in range(len(s)):
    print(colored(f"Test {(test + 1)}:", "green"), minCut(s[test]), "|", colored("Passed", "green"))
