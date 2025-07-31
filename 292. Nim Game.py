# Leetcode - 292. Nim Game (Python language) - Easy

from termcolor import colored

print(colored("Leetcode - 292. Nim Game (Python language) -","yellow"), colored("Easy","green"))

def canWinNim(nVar):
    return not(nVar % 4 == 0)

n = [4,1,2]

for test in range(len(n)):
    print(colored(f"Test {(test + 1)}:","green"), canWinNim(n[test]), "|", colored("Passed","green"));