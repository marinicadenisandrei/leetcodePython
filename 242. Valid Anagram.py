# Leetcode - 242. Valid Anagram (Python language) - Easy

from termcolor import colored
print(colored("Leetcode - 242. Valid Anagram (Python language) -", "yellow"), colored("Easy", "green"))

def isAnagram(sVar, tVar):
    return "".join(sorted(sVar)) == "".join(sorted(tVar)) 
    
s = ["anagram","rat"]
t = ["nagaram","car"]

for test in range(len(s)):
    print(colored(f"Test {(test + 1)}:", "green"), isAnagram(s[test], t[test]), "|", colored("Passed","green"))    

