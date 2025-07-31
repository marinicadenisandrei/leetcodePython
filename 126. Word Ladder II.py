# Leetcode - 126. Word Ladder II (Python language) - Hard

from termcolor import colored

print(colored("Leetcode - 126. Word Ladder II (Python language) -", "yellow"), colored("Hard", "red"))

def findLadders(wordListVar, beginWordVar, endWordVar):
    if endWordVar not in wordListVar:
        return []
    
    wordListVar.insert(0, beginWord)
    potential = [i for i in wordListVar if len(set(i).intersection(set(endWordVar))) == len(endWordVar) - 1]

    output = []

    for i in range(len(potential)):
        output.append([])

        set1 = set(str(beginWordVar))
        set2 = set(str(endWordVar))
        same = len(set1.intersection(set2))
        offset = wordListVar.index(potential[i])

        for j in range(offset + 1):
            set1 = set(str(wordListVar[j]))
            set2 = set(str(endWordVar))
            newSame = len(set1.intersection(set2))

            if newSame >= same:
                same = newSame
                output[i].append(wordListVar[j])
            
            if same == len(endWordVar) - 1:
                output[i].append(endWordVar)
                wordListVar = [k for k in wordListVar if k[0] != potential[i][0]]
                break
        
    return output
    
wordList = [["hot","dot","dog","lot","log","cog"], ["hot","dot","dog","lot","log"]]
beginWord = ["hit", "hit"]
endWord = ["cog", "cog"]

for test in range(len(endWord)):
    testNumber = test + 1
    print(colored(f"Test {testNumber}:", "green"), findLadders(wordList[test], beginWord[test], endWord[test]), "|", colored("Passed", "green"))
