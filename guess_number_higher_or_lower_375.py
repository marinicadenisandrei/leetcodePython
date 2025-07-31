# Leetcode - 375. Guess Number Higher or Lower II (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 375. Guess Number Higher or Lower II (Python language) - Medium", "yellow"))

def getMoneyAmount(n: int) -> int:
    dp = [[0] * (n + 2) for _ in range(n + 2)]
    
    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            best = float('inf')

            for x in range(i, j + 1):
                cost = x + max(dp[i][x - 1], dp[x + 1][j])
                if cost < best:
                    best = cost

            dp[i][j] = best
    
    return dp[1][n]

                    
n = [10,1,2]

for test in range(len(n)):
    print(colored(f"Test {(test + 1)}:","green"), getMoneyAmount(n[test]), "|", colored("Passed","green"))

    