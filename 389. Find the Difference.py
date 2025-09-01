# Leetcode - 389. Find the Difference (Python language) - Easy

from termcolor import colored

print(colored("Leetcode - 389. Find the Difference (Python language) -","yellow"), colored("Easy","green"))

def findTheDifference(sVar, tVar):
    return list(set(tVar) - set(sVar))[0]

s = ["abcd",""]
t = ["abcde","y"]

for test in range(len(s)):
    print(
        colored(f"Test {(test + 1)}:","green"),
        findTheDifference(s[test], t[test]),
        "|",
        colored("Passed","green")
    )
    