# Leetcode - 451. Sort Characters By Frequency (Python language) - Medium

from collections import Counter
from termcolor import colored

print(colored("Leetcode - 451. Sort Characters By Frequency (Python language) - Medium", "yellow"))

def frequencySort(sVar):
    freq = Counter(sVar)
    return ''.join(sorted(sVar, key=lambda c: freq[c], reverse=True))

s = ["tree","cccaaa","Aabb"]

for test in range(len(s)):
    print(
        colored(f"Test {(test + 1)}:", "green"),
        frequencySort(s[test]),
        "|",
        colored("Passed", "green")
    )