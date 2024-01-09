# Leetcode - 139. Word Break (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 139. Word Break (Python language) - Medium", "yellow"))

def wordBreak(sVar: str, wordDictVar : str):
    for i in wordDictVar:
        sVar = sVar.replace(i, "")

    if len(sVar) == 0:
        return True
    
    return False

s = ["leetcode", "applepenapple", "catsandog"]
wordDict = [["leet","code"], ["apple","pen"], ["cats","dog","sand","and","cat"]]

for test in range(len(s)):
    print(colored(f"Test {(test + 1)}:", "green"), wordBreak(s[test], wordDict[test]), "|", colored("Passed", "green"))
