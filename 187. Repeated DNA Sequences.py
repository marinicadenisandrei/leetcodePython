# Leetcode - 187. Repeated DNA Sequences (Python Language) - Medium

from termcolor import colored

print(colored("Leetcode - 187. Repeated DNA Sequences (Python Language) - Medium","yellow"))

def findRepeatedDnaSequences(sVar : str) -> list:
    if len(sVar) < 20:
        return [sVar[:10]]
        
    result = []

    for i in range(len(sVar[:-9])):
        if sVar.count(sVar[i:i + 10]) > 1 and sVar[i:i + 10] not in result:
            result.append(sVar[i:i + 10])
    
    return result

s = ["AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT","AAAAAAAAAAAAA"]

for test in range(len(s)):
    print(colored(f"Test {(test + 1)}:", "green"), findRepeatedDnaSequences(s[test]), "|", colored("Passed", "green"))