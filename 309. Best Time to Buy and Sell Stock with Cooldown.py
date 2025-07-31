# Leetcode - 309. Best Time to Buy and Sell Stock with Cooldown (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 309. Best Time to Buy and Sell Stock with Cooldown (Python language) - Medium","yellow"))

def maxProfit(pricesVar):
    if len(pricesVar) < 2:
        return 0

    buyIndex = []
    resultCandidates = []

    pricesVar.append(0)
    element = pricesVar[0]
    profit = 0

    for i in range(1,len(pricesVar) - 1):
        if pricesVar[i] > pricesVar[i + 1]:
            profit += (pricesVar[i] - element)
            element = pricesVar[i + 1]
            buyIndex.append(i)
            continue
        
    for i in buyIndex:
        newResult = profit - (pricesVar[i] - pricesVar[i - 1])
        resultCandidates.append(newResult)

    return max(resultCandidates)

prices = [[1,2,3,0,2],[1]]

for test in range(len(prices)):
    print(colored(f"Test {(test + 1)}:","green"), maxProfit(prices[test]),"|",colored("Passed","green"))