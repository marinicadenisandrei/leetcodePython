# Leetcode - 434. Number of Segments in a String (Python language) - Easy

from termcolor import colored

print(colored(f"Leetcode - 434. Number of Segments in a String (Python language) -", "yellow"), colored("Easy", "green"))

def countSegments(sVar):
    return len(sVar.split(" "))

s = ["Hello, my name is John", "Hello"]

for test in range(len(s)):
    print(
        colored(f"Test {(test + 1)}:", "green"),
        countSegments(s[test]),
        "|",
        colored("Passed","green")
    )