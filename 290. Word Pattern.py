# Leetcode - 290. Word Pattern (Python language) - Easy

from termcolor import colored

print(colored("Leetcode - 290. Word Pattern (Python language) -","yellow"), colored("Easy","green"))

def wordPattern(patternVar, sVar):
    patternVar = [i for i in patternVar]
    sVar = sVar.split(" ")

    patternVar = list(dict.fromkeys(patternVar))
    sVar = list(dict.fromkeys(sVar))
    
    if len(patternVar) == len(sVar):
        return True
    
    return False
        
pattern = ["abba", "abba", "aaaa"]
s = ["dog cat cat dog","dog cat cat fish","dog cat cat dog"]

for test in range(len(pattern)):
    print(colored(f"Test {(test + 1)}:","green"), wordPattern(pattern[test], s[test]), "|", colored("Passeed","green"))