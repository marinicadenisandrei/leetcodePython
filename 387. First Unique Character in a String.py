# Leetcode - 387. First Unique Character in a String (Python language) - Easy

from termcolor import colored

print(colored("Leetcode - 387. First Unique Character in a String (Python language) -","yellow"), colored("Easy","green"))

def firstUniqChar(sVar):
    for i in range(len(sVar)):
        if sVar.count(sVar[i]) == 1:
            return i
        
    return -1
            
s = ["leetcode","loveleetcode","aabb"]

for test in range(len(s)):
    print(
        colored(f"Test {(test + 1)}:","green"),
        firstUniqChar(s[test]),
        "|",
        colored("Passed","green")
    )
    