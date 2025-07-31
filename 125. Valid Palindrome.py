from termcolor import colored

print(colored("Leetcode 125. Valid Palindrome (Python language) -", "yellow"), colored("Easy", "green"))

def isPalindrome(sVar):
    sVar = sVar.replace(" ","")
    sVar = "".join(i for i in sVar if i.isalnum())
    sVar = sVar.lower()

    if sVar == sVar[::-1]:
        return True
    
    return False 

s = ["A man, a plan, a canal: Panama", "race a car", " "]

for test in range(len(s)):
    testNumber = test + 1
    print(colored(f"Test {testNumber}:", "green"), isPalindrome(s[test]), "|", colored("Passed", "green"))