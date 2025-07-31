# Leetcode - 188. Best Time to Buy and Sell Stock IV (Pythin language) - Hard

from termcolor import colored

print(colored("Leetcode - 188. Best Time to Buy and Sell Stock IV (Pythin language) -","yellow"),colored("Hard","red"))

def maxProfit(pricesVar: list, kVar: int):
    for j in range(len(pricesVar)):
        buyDay = pricesVar[j]
        profit = 0
        counter = 0
        
        for i in range(j,len(pricesVar) - 1):
            if pricesVar[i] > pricesVar[i + 1]:
                profit += (pricesVar[i] - buyDay)
                continue
                
            if pricesVar[i] < pricesVar[i + 1]:
                buyDay = pricesVar[i]
                counter += 1
                
        if counter >= kVar - 1:
            return profit

prices = [[2,4,1],[3,2,6,5,0,3]]
k = [2,2]

for test in range(len(prices)):
    print(colored(f"Test {(test + 1)}:","green"),maxProfit(prices[test], k[test]),"|",colored("Passed"))