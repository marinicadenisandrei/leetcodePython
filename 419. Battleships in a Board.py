# Leetcode - 419. Battleships in a Board (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 419. Battleships in a Board (Python language) - Medium", "yellow"))

def countBattleships(boardVar):
    result = 0

    for i in range(len(boardVar)):
        for j in range(len(boardVar[i])):
            if boardVar[i][j] == "X":
                final_i = 0
                final_j = 0
                
                for k in range(len(boardVar)):
                    if boardVar[k][j] == ".":
                        final_i = k
                        break
                    elif k == len(boardVar) - 1:
                        final_i = k + 1
                        break
                
                for k in range(len(boardVar[i])):
                    if boardVar[i][k] == ".":
                        final_j = k
                        break
                    elif k == len(boardVar[i]) - 1:
                        final_j = k + 1
                        break
                
                if i > final_i and final_i == 0:
                    final_i = i + 1
                
                if j > final_j and final_j == 0:
                    final_j = j + 1
                
                for k in range(i, final_i):
                    for l in range(j, final_j):
                        boardVar[k][l] = "."

                result += 1
    
    return result

board = [[["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]],[["."]]]

for test in range(len(board)):
    print(
        colored(f"Test {(test + 1)}:", "green"),
        countBattleships(board[test]),
        "|",
        colored("Passed", "green")
    )
