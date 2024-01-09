# Leetcode - 126. Word Ladder II (Python language) - Hard

from termcolor import colored

print(colored("Leetcode - 126. Word Ladder II (Python language) -", "yellow"), colored("Hard", "red"))

def ladderLength(wordListVar, beginWordVar, endWordVar):
    if endWordVar not in wordListVar:
        return 0

    output = []
    potential = [i for i in wordListVar if len (set(i).intersection(set(endWordVar))) == len(endWordVar) - 1]

    for i in range(len(potential)):
        output.append([beginWordVar]);
        intersection = 0 

        for j in range(len(wordListVar) - wordListVar.index(potential[i]) + 1):
            if intersection <= len(set(wordListVar[j]).intersection(set(endWordVar))):
                output[i].append(wordListVar[j])
                intersection = len(set(wordListVar[j]).intersection(set(endWordVar)))
            else:
                break
        
        output[i].append(endWordVar)
        wordListVar = [k for k in wordListVar if k[0] != potential[i][0]]

    minVar = len(min(output, key=len))
    return minVar

wordList = [["hot","dot","dog","lot","log","cog"], ["hot","dot","dog","lot","log"]]
beginWord = ["hit", "hit"]
endWord = ["cog", "cog"]

for test in range(len(beginWord)):
    testNumber = test + 1
    print(colored(f"Test {testNumber}:", "green"), ladderLength(wordList[test], beginWord[test], endWord[test]), "|", colored("Passed", "green"))

