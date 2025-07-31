# Leetcode - 122. Best Time to Buy and Sell Stock II (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 122. Best Time to Buy and Sell Stock II (Python language) - Medium", "yellow"))

def maxProfit(pricesVar):
    profit = 0

    is_ascending = lambda pricesVar: all(pricesVar[i] <= pricesVar[i + 1] for i in range(len(pricesVar) - 1))
    is_descending = lambda pricesVar: all(pricesVar[i] >= pricesVar[i + 1] for i in range(len(pricesVar) - 1))

    if is_ascending(pricesVar):
        return pricesVar[-1] - pricesVar[0]
    elif is_descending(pricesVar):
        return 0

    for i in range(1,len(pricesVar)):
        if pricesVar[i] - pricesVar[i - 1] > 0:
            maximVar = pricesVar[i] - pricesVar[i - 1]

            for j in range(i, len(pricesVar)):
                if pricesVar[j] < pricesVar[i]:
                    profit += maximVar
                    maximVar = 0
                    i += j
                    break
                else:
                    maximVar = pricesVar[j] - pricesVar[i - 1]
                    
    return profit

prices = [[7,1,5,3,6,4],[1,2,3,4,5],[7,6,4,3,1]]

for test in range(len(prices)):
    testNumber = test + 1
    print(colored(f"Test {testNumber}:", "green"), maxProfit(prices[test]), "|", colored("Passed", "green"))

