# Leetcode - 123. Best Time to Buy and Sell Stock III (Python language) - Hard

from termcolor import colored

print(colored("Leetcode - 123. Best Time to Buy and Sell Stock III (Python language) -", "yellow"), colored("Hard","red"))

def maxProfit(pricesVar):
    ascending = lambda lst: all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))
    descending = lambda lst: all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1))

    if ascending(pricesVar):
        return pricesVar[-1] - pricesVar[0]
        
    if descending(pricesVar):
        return 0
        
    pricesVar.append(0)
    minimumIndex = pricesVar.index(min(pricesVar))
    maximVar = pricesVar[minimumIndex]
    profit = 0
    
    for i in range(minimumIndex,len(pricesVar)):
        if pricesVar[i] >= maximVar:
            maximVar = pricesVar[i]
        else:
            profit += maximVar - pricesVar[minimumIndex]
            minimumIndex = i

    return profit
    
prices = [[3,3,5,0,0,3,1,4], [1,2,3,4,5], [7,6,4,3,1]]

for test in range(len(prices)):
    testNumber = test + 1
    print(colored(f"Test {testNumber}:", "green"), maxProfit(prices[test]), "|", colored("Passed", "green"))