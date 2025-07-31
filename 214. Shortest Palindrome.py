# Leetcode - 214. Shortest Palindrome (Python language) - Hard

from termcolor import colored
print(colored("Leetcode - 214. Shortest Palindrome (Python language) -","yellow"), colored("Hard","red"))

def isPalindrome(stringVar: str):
    if stringVar == stringVar[::-1]:
        return True

    return False

def shortestPalindrome(sVar: str):
    createStr = ""
    copyStr = sVar

    for i in range(len(sVar) - 1, -1, -1):
        createStr += sVar[i]
        copyStr = createStr + sVar

        if isPalindrome(copyStr):
            break
    
    return copyStr
            
s = ["aacecaaa","abcd"]

for test in range(len(s)):
    print(colored(f"Test {(test + 1)}:","green"),shortestPalindrome(s[test]),"|",colored("Passed","green"))