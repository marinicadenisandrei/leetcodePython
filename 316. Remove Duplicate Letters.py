# Leetcode - 316. Remove Duplicate Letters (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 316. Remove Duplicate Letters (Python language) - Medium","yellow"))

def removeDuplicateLetters(sVar):
    sVar = list(dict.fromkeys(list(sVar)))
    sVar.sort()

    return "".join(sVar)


s = ["bcabc","cbacdcbc"]

for test in range(len(s)):
    print(colored(f"Test {(test + 1)}:","green"), removeDuplicateLetters(s[test]), "|", colored("Passed","green"))