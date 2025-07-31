# Leetcode - 383. Ransom Note (Python language) - Easy

from termcolor import colored
from collections import Counter

print(colored("Leetcode - 383. Ransom Note (Python language) -", "yellow"), colored("Easy","green"))

def canConstruct(ransomNoteVar, magazineVar):
    return Counter(ransomNoteVar) <= Counter(magazineVar)

ransomNote = ["a","aa","aa"]
magazine = ["b","ab","aab"]

for test in range(len(ransomNote)):
    print(
        colored(f"Tst {(test + 1)}:", "green"),
        canConstruct(ransomNote[test], magazine[test]),
        "|",
        colored("Passed","green")
    )
    