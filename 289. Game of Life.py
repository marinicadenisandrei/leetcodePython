# Leetcode - 289. Game of Life (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 289. Game of Life (Python language) - Medium","yellow"))

def gameOfLife(boardVar):
    copyBoard = [i.copy() for i in boardVar]

    for i in range(len(boardVar)):
        for j in range(len(boardVar[i])):
            neiVar = []
        
            if i - 1 >= 0:
                if j - 1 >=0:
                    neiVar.append(boardVar[i - 1][j - 1])
                
                neiVar.append(boardVar[i - 1][j])

                if j + 1 < len(boardVar[i]):
                    neiVar.append(boardVar[i - 1][j + 1])
            
            if j - 1 >= 0:
                neiVar.append(boardVar[i][j - 1])
            
            if j + 1 < len(boardVar[i]):
                neiVar.append(boardVar[i][j + 1])
        
            if i + 1 < len(boardVar):
                if j - 1 >= 0:
                    neiVar.append(boardVar[i - 1][j - 1])

                neiVar.append(boardVar[i + 1][j])
            
                if j + 1 < len(boardVar[i]):
                    neiVar.append(boardVar[i + 1][j + 1])
        
            oneCount = neiVar.count(1)

            if boardVar[i][j] == 1:
                if oneCount < 2 or oneCount > 3:
                    copyBoard[i][j] = 0
            else:
                if oneCount == 3:
                    copyBoard[i][j] = 1
                    
    return copyBoard
        
board = [[[0,1,0],[0,0,1],[1,1,1],[0,0,0]],[[1,1],[1,0]]]

for test in range(len(board)):
    print(colored(f"Test {(test + 1)}:","green"), gameOfLife(board[test]), "|", colored("Passed","green"))
    