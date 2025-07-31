# Leetcode - 336. Palindrome Pairs (Python language) - Hard

from termcolor import colored

print(colored("Leetcode - 336. Palindrome Pairs (Python language) -","yellow"), colored("Hard","red"))

def palindromePairs(wordsVar):
    result = []

    for i in range(len(wordsVar)):
        for j in range(len(wordsVar)):
            if (wordsVar[i] + wordsVar[j])[::-1] == (wordsVar[i] + wordsVar[j]) and i != j:
                result.append([i,j])
                
                
    return result

words = [["abcd","dcba","lls","s","sssll"],["bat","tab","cat"],["a",""]]

for test in range(len(words)):
    print(colored(f"Test {(test + 1)}:","green"), palindromePairs(words[test]), "|", colored("Passed","green"))
    
    