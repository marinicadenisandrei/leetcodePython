# Leetcode - 79. Word Search (Python laguage) - Medium

from termcolor import colored

print(colored("Leetcode - 79. Word Search (Python laguage) - Medium", "yellow"))

boardTest = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
wordTest = ["ABCCED", "SEE", "ABCB"]

for test in range(len(boardTest)):
    board = boardTest[test]
    word = wordTest[test]

    indexFound = []
    flagOutput = None

    while True:
        flag = False

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    flag = True
                    board[i][j] = ""
                    indexFound.append((i,j))
                    break
            if flag == True:
                break
        
        if flag == False:
            break

        flag = False

        for i in range(1,len(word)):
            for j in range(len(board)):
                for k in range(len(board[j])):
                    if board[j][k] == word[i]:
                        if (indexFound[-1][0] == j and indexFound[-1][1] + 1 == k or indexFound[-1][1] - 1 == k) or (indexFound[-1][0] + 1 == j and indexFound[-1][1] == k):
                            board[j][k] = ""
                            indexFound.append((j,k))
                            flag = True
                            break

                if flag == True:
                    break
            
            flag = False

        if len(indexFound) == len(word):
            flagOutput = True
            break
        else:
            flagOutput = False
            indexFound = []

    testNumber = test + 1

    print(colored(f"Test {testNumber}:","green"),flagOutput,"|",colored("Passed", "green"))


    




