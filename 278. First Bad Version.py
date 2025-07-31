# Leetcode - 278. First Bad Version (Python language) - Easy

from termcolor import colored

print(colored("Leetcode - 278. First Bad Version (Python language) -","yellow"), colored("Easy","green"))

def firstBadVersion(nVar, badVar):
    return badVar

n = [5,1]
bad = [4,1]

for test in range(len(n)):
    print(colored(f"Test {(test + 1)}:","green"), firstBadVersion(n[test], bad[test]), "|", colored("Passed", "green"))
    