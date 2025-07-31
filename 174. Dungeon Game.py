# Leetcode - 174. Dungeon Game (Python language) - Hard

from termcolor import colored

print(colored("Leetcode - 174. Dungeon Game (Python language) -", "yellow"), colored("Hard", "red"))

def calculateMinimumHP(dungeonVar: list):
    dungeonVar[-1][-1] = 1 - dungeonVar[-1][-1]

    for i in reversed(range(len(dungeonVar[-1]) - 1)):
        dungeonVar[-1][i] = max(1,dungeonVar[-1][i + 1] - dungeonVar[-1][i])
    
    for i in reversed(range(len(dungeonVar) - 1)):
        dungeonVar[i][-1] = max(1, dungeonVar[i + 1][-1] - dungeonVar[i][-1])

    for i in reversed(range(len(dungeonVar) - 1)):
        for j in reversed(range(len(dungeonVar[i]) - 1)):
            dungeonVar[i][j] = max(min(dungeonVar[i + 1][j], dungeonVar[i][j + 1]), min(dungeonVar[i + 1][j], dungeonVar[i][j + 1]) - dungeonVar[i][j])

    return dungeonVar[0][0]

dungeon = [[[-2,-3,3],[-5,-10,1],[10,30,-5]],[[0]]]

for test in range(len(dungeon)):
    print(colored(f"Test {(test + 1)}:", "green"), calculateMinimumHP(dungeon[test]), "|", colored("Passed", "green"))