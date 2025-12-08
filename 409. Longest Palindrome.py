# Leetcode - 409. Longest Palindrome (Python language) - Easy

from termcolor import colored

print(colored("Leetcode - 409. Longest Palindrome (Python language) -", "yellow"), colored("Easy", "green"))

def isPalindrome(sVar):
    return sVar == sVar[::-1]

def longestPalindrome(sVar):
    counts = {}
    flagAddOne = False
    result = 0

    for ch in sVar:
        if ch not in counts:
            counts[ch] = 1
        else:
            counts[ch] += 1
    
    for key, value in counts.items():
        if value % 2 == 0:
            result += value
        else:
            result += value - 1
            if not flagAddOne:
                flagAddOne += 1
    
    if flagAddOne:
        result += 1
    
    return result

s = ["abccccdd","a"]

for test in range(len(s)):
    print(
        colored(f"Test {(test + 1)}:","green"),
        longestPalindrome(s[test]),
        "|",
        colored("Passed","green")
    )