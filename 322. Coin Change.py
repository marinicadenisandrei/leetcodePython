# Leetcode - 322. Coin Change (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 322. Coin Change (Python language) - Medium","yellow"))

def CoinChange(coinsVar, amountVar):
    if amountVar == 0:
        return 0
        
    flag = True
    c = 0

    while amountVar > 0:
        flag = False
        for i in coinsVar[::-1]:
            if amountVar >= i:
                amountVar -= i
                flag = True
                c += 1
                break
        
        if not flag:
            return -1
    
    return c
            
coins = [[1,2,5],[2],[1]]
amount = [11,3,0]

for test in range(len(coins)):
    print(colored(f"Test {(test + 1)}:","green"), CoinChange(coins[test], amount[test]), "|", colored("Passed","green"))