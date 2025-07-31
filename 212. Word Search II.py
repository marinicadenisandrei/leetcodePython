# Leetcode - 212. Word Search II (Python language) - Hard

from termcolor import colored
print(colored("Leetcode - 212. Word Search II (Python language) -","yellow"), colored("Hard","red"))

def findWords(boardVar: list, wordsVar: list):
    results = []

    for i in range(len(wordsVar)):
        indexes = []
        flag = True
        stringVerification = ""

        for j in range(len(wordsVar[i])):
            for k in boardVar:
                if wordsVar[i][j] in k:
                    stringVerification += wordsVar[i][j]
                    indexes.append([j,k.index(wordsVar[i][j])])
        
        for j in range(len(indexes) - 1):
            if abs(indexes[j][0] - indexes[j + 1][0]) > 1 or abs(indexes[j][1] - indexes[j + 1][1]) > 1:
                flag = False
                break 
        
        stringVerification = ''.join(set(stringVerification))
        stringVerification = sorted(stringVerification)

        sortedWord = sorted(wordsVar[i])

        if flag and sortedWord == stringVerification:
            results.append(wordsVar[i])
        
    return results
            

board = [[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],[["a","b"],["c","d"]]]
words = [["oath","pea","eat","rain"],["abcb"]]

for test in range(len(board)):
    print(colored(f"Test {(test + 1)}:","green"), findWords(board[test], words[test]), "|", colored("Passed","green"))