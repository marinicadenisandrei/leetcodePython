# Leetcdoe - 392. Is Subsequence (Python language) - Easy

from termcolor import colored

print(colored("Leetcdoe - 392. Is Subsequence (Python language) -","yellow"), colored("Easy","green"))

def isSubsequence(sVar, tVar):
    return ''.join(sorted(sVar)) == ''.join(sorted(tVar))[:len(sVar)]

s = ["abc","axc"]
t = ["ahbgdc","ahbgdc"]

for test in range(len(s)):
    print(
        colored(f"Test {(test + 1)}:", "green"),
        isSubsequence(s[test], t[test]),
        "|",
        colored("Easy","green")
    )
    