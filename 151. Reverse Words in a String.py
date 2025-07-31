# Leetcode - 151. Reverse Words in a String (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 151. Reverse Words in a String (Python language) - Medium","yellow"))

def reverseWords(sVar : str):
    sVar = sVar.split(" ")[::-1]
    sVar = [i for i in sVar if len(i) > 0]
    sVar = " ".join(sVar)

    return sVar

s = ["the sky is blue", "  hello world  ", "a good   example"]

for test in range(len(s)):
    print(colored(f"Test {(test + 1)}:", "green"), reverseWords(s[test]), "|", colored("Passed", "green"))