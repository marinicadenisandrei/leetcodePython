# Leetcode - 459. Repeated Substring Pattern (Python language) - Easy

from termcolor import colored

print(colored("Leetcode - 459. Repeated Substring Pattern (Python language) -", "yellow"), colored("Easy", "green"))

def repeatedSubstringPattern(sVar):
    for i in range(1, len(sVar)):
        substring = sVar[:i]
        check = sVar[i:]

        if check.replace(substring, "") == "":
            return True

    return False


s = ["abab","aba","abcabcabcabc"]

for test in range(len(s)):
    print(
        colored(f"Test {(test + 1)}:", "green"),
        repeatedSubstringPattern(s[test]),
        "|",
        colored("Passed", "green")
    )