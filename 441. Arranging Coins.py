# Leetcode - 441. Arranging Coins (Python language) - Easy

from termcolor import colored

print(colored("Leetcode - 441. Arranging Coins (Python language) -", "yellow"), colored("Easy", "green"))

def arrangeCoins(nVar):
    counter = 1

    while nVar > 0:
        if nVar >= counter:
            nVar -= counter
            counter += 1
        else: 
            return counter - 1
    
    return 0

n = [5,8]

for test in range(len(n)):
    print(
        colored(f"Test {(test + 1)}:", "green"),
        arrangeCoins(n[test]),
        "|",
        colored("Passed", "green")
    )