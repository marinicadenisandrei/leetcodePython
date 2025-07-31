# Leetcode - 200. Number of Islands (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 200. Number of Islands (Python language) - Medium", "yellow"))

def numIslands(gridVar: list):
    counter = 0
    right_above = 0
    left_bottm = 0

    for i in range(len(gridVar)):
        for j in range(len(gridVar[i])):
            if gridVar[i][j] == "1":
                for k in range(j,len(gridVar[i])):
                    if gridVar[i][k] == "0":
                        right_above = k
                        break

                    if k == len(gridVar[i]) - 1:
                        right_above = k + 1
                        break
                
                for k in range(i,len(gridVar)):
                    if gridVar[k][i] == "0":
                        left_bottm = k
                        break
                    
                    if k == len(gridVar) - 1:
                        left_bottm = k + 1
                        break
                    
                for k in range(i, left_bottm):
                    for l in range(j, right_above):
                        gridVar[k][l] = "x"

                counter += 1
    
    return counter

grid = [[
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
], [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]]

for test in range(len(grid)):
    print(colored(f"Test {(test + 1)}:", "green"), numIslands(grid[test]), "|", colored("Passed","green"))