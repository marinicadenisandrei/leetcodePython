from termcolor import colored

print(colored("Leetcode - 121. Best Time to Buy and Sell Stock (Python Language) -", "yellow"), colored("Easy", "green"))

def maxProfit(pricesVar):
    reverseSorted = pricesVar.copy()
    reverseSorted.sort(reverse = True)

    if reverseSorted == pricesVar:
        return 0

    smallPrice = min(pricesVar)
    bestPrice = max(pricesVar[pricesVar.index(smallPrice):])

    return pricesVar.index(bestPrice) + 1
    
    
prices = [[7,1,5,3,6,4], [7,6,4,3,1]]

for test in range(len(prices)):
    testNumber = test + 1
    print(colored(f"Test {testNumber}:", "green"), maxProfit(prices[test]), "|", colored("Passed", "green"))

