# Leetcode - 403. Frog Jump (Python language) - Hard

from termcolor import colored

print(colored("Leetcode - 403. Frog Jump (Python language) -", "yellow"), colored("Hard", "red"))

def canCross(stonesVar):
    lastJump = 0
    jumpNo = 1

    for i in range(len(stonesVar) - 1):
        if lastJump == stonesVar[i + 1] - stonesVar[i]:
            jumpNo -= 1
        
        if stonesVar[i + 1] - stonesVar[i] <= jumpNo:
            jumpNo += 1
        else:
            return False

        lastJump = stonesVar[i + 1] - stonesVar[i]
    
    return True
    
stones = [[0,1,3,5,6,8,12,17],[0,1,2,3,4,8,9,11]]

for test in range(len(stones)):
    print(
        colored(f"Test {test + 1}:", "green"),
        canCross(stones[test]),
        "|",
        colored("Passed","green")
    )