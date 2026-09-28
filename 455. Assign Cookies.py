# Leetcode - 455. Assign Cookies (Python language) - Easy

from termcolor import colored

print(colored("Leetcode - 455. Assign Cookies (Python language) -", "yellow"), colored("Easy", "green"))

def findContentChildren(gVar, sVar):
    gVar = sorted(gVar)
    sVar = sorted(sVar)

    i = 0
    j = 0

    while i < len(gVar) and j < len(sVar):
        if sVar[j] >= gVar[i]:
            i += 1

        j += 1

    return i

g = [[1,2,3],[1,2]]
s = [[1,1],[1,2,3]]

for test in range(len(g)):
    print(
        colored(f"Test {(test + 1)}:", "green"),
        findContentChildren(g[test], s[test]),
        "|",
        colored("Passed", "green")
    )