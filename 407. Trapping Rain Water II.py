# Leetcode - 407. Trapping Rain Water II (Python language) - Hard

from termcolor import colored

print(colored("Leetcode - 407. Trapping Rain Water II (Python language) -", "yellow"), colored("Hard", "red"))

def count_vertical_trapped_x(board, num):
    rows = len(board)
    cols = len(board[0])
    count = 0

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'X':
                above = False
                for rr in range(r - 1, -1, -1):
                    if board[rr][c] == num:
                        above = True
                        break

                below = False
                for rr in range(r + 1, rows):
                    if board[rr][c] == num:
                        below = True
                        break

                if above and below:
                    count += 1

    return (count > 0, count)

def trapRainWater(heightMapVar):
    starterMap = [[1 for _ in row] for row in heightMapVar]
    level = 2
    result = 0

    while not all(x == 'X' for row in starterMap for x in row):
        for i in range(len(starterMap)):
            for j in range(len(starterMap[i])):
                if level > heightMapVar[i][j]:
                    starterMap[i][j] = 'X'
                else:
                    starterMap[i][j] = level

        status = count_vertical_trapped_x(starterMap, level)

        if status[0] == True:
            result += status[1]

        level += 1
    
    return result

heightMap = [[[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]],[[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]]

for test in range(len(heightMap)):
    print(
        colored(f"Test {(test + 1)}:","green"),
        trapRainWater(heightMap[test]),
        "|",
        colored("Passed", "green")
    )