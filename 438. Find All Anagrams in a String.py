# Leetcode - 438. Find All Anagrams in a String (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 438. Find All Anagrams in a String (Python language) - Medium","yellow"))

def findAnagrams(sVar, pVar):
    result = []

    pVar = ''.join(sorted(pVar))

    for i in range(len(sVar) - len(pVar)):
        candidate = ''.join(sorted(sVar[i:i + len(pVar)]))
        
        if candidate == pVar:
            result.append(i)
    
    return result

s = ["cbaebabacd","abab"]
p = ["abc","ab"]

for test in range(len(s)):
    print(
        colored(f"Test {(test + 1)}:", "green"),
        findAnagrams(s[test], p[test]),
        "|",
        colored("Passed","green")
    )