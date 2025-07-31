# Leetcode - 344. Reverse String (Python language) - Easy

from termcolor import colored

print(colored("Leetcode - 344. Reverse String (Python language) -","yellow"), colored("Easy","green"))

def reverseString(sVar):
    return sVar[::-1]

s = [["h","e","l","l","o"],["H","a","n","n","a","h"]]

for test in range(len(s)):
    print(colored(f"Test {(test + 1)}:","green"), reverseString(s[test]), "|", colored("Passed","green"))
    
    