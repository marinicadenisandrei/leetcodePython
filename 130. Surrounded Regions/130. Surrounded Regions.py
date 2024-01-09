# Leetcode - 130. Surrounded Regions (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 130. Surrounded Regions (Python language) - Medium", "yellow"))

def solve(boardVar: list):
    for i in range(1,len(boardVar) - 1):
        for j in range(1, len(boardVar) - 1):
            if boardVar[i][j] == "O":
                if boardVar[i][j-1] == "X" or boardVar[i-1][j] == "X" or boardVar[i][j+1] == "X" or boardVar[i+1][j] == "X":
                    boardVar[i][j] = "X"
                    
board = [[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]], [["X"]]]

for test in range(len(board)):    
    solve(board[test])
    print(colored(f"Test {(test + 1)}:", "green"), board[test], "|", colored("Passed", "green"))