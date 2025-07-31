# Leetcode - 205. Isomorphic Strings (Python language) - Easy

from termcolor import colored

print(colored("Leetcode - 205. Isomorphic Strings (Python language) -", "yellow"), colored("Easy","green"))

def isIsomorphic(sVar: str, tVar: str):
    counter_s = 1
    counter_t = 1

    for i in range(len(sVar) - 1):
        if sVar[i] == sVar[i + 1]:
            counter_s += 1
        
        if tVar[i] == tVar[i + 1]:
            counter_t += 1
        else:
            if counter_s != counter_t:
                return False
                
            counter_s = 1
            counter_t = 1
    
    if counter_s != counter_t:
        return False

    return True
            
s = ["egg","foo","paper"]
t = ["add","bar","title"]

for test in range(len(s)):
    print(colored(f"Test {(test + 1)}:", "green"), isIsomorphic(s[test], t[test]), "|", colored("Easy", "green"))