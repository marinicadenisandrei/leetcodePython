# Leetcode - 318. Maximum Product of Word Lengths (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 318. Maximum Product of Word Lengths (Python language) - Medium","yellow"))

def maxProduct(wordsVar):
    result = 0

    for i in wordsVar:
        for j in wordsVar:
            if not (set(i) & set(j)) and len(i) * len(j) > result:
                result = len(i) * len(j)          

    return result
                    
words = [["abcw","baz","foo","bar","xtfn","abcdef"],["a","ab","abc","d","cd","bcd","abcd"],["a","aa","aaa","aaaa"]]

for test in range(len(words)):
    print(colored(f"Test {(test + 1)}:","green"), maxProduct(words[test]), "|", colored("Passed","green"))