# Leetcode - 197. Rising Temperature (Python language) - Easy

from termcolor import colored

print(colored("Leetcode - 197. Rising Temperature (Python language) -","yellow"), colored("Easy","green"))

def risingTemperature(idVar: list, temperatureVar: list):
    for i in range(0,len(idVar),2):
        if temperatureVar[i] < temperatureVar[i+1]:
            print(idVar[i + 1])
        

id = [1,2,3,4]
temperature = [10,25,20,30]

print(colored("Test 1:", "green"))
risingTemperature(id, temperature)
print(colored("| Passed","green"))