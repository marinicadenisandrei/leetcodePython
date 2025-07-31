# Leetcode - 135. Candy (C language) - Hard

from termcolor import colored

print(colored("Leetcode - 135. Candy (C language) -", "yellow"), colored("Hard", "red"))

def candy(ratingsVar : list):
    candyVar = [1 for _ in range(len(ratingsVar))]
    
    if ratingsVar[0] >= ratingsVar[1]:
        candyVar[0] += 1

    if ratingsVar[-1] >= ratingsVar[-2]:
        candyVar[-1] += 1
        
    for i in range(1, len(ratingsVar) - 1):
        if ratingsVar[i] > ratingsVar[i + 1] and ratingsVar[i] > ratingsVar[i - 1]:
            candyVar[i] += 1

    return sum(candyVar)

ratings = [[1,0,2], [1,2,2]]

for test in range(len(ratings)):
    print(colored(f"Test {(test + 1)}:", "green"), candy(ratings[test]), "|", colored("Passed", "green"))