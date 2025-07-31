# Leetcode - 273. Integer to English Words (Python language) - Hard

from termcolor import colored
print(colored("Leetcode - 273. Integer to English Words (Python language) -","yellow"), colored("Hard","red"))

def numberToWords(numVar):
    usualNumbers = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve"]
    secondNumbers = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
    thirdNumbers = ["", "Thousand ", "Million"]

    numVar = str(numVar)
    acumulation = []
    result = ""

    while len(numVar) > 2:
        acumulation.append(numVar[-3:])
        numVar = numVar[:-3]
    
    for i in range(len(acumulation)):
        result = usualNumbers[int(acumulation[i][0])] + " " + "Hundred" + " " + secondNumbers[int(acumulation[i][1])] + " " + usualNumbers[int(acumulation[i][2])] + " " + thirdNumbers[i] + " " + result

    if len(numVar) > 0:
        result = usualNumbers[int(numVar)] + " " + thirdNumbers[len(acumulation)] + " " + result     

    return result
    

num = [123,12345,1234567]

for test in range(len(num)):
    print(colored(f"Test {(test + 1)}:","green"), numberToWords(num[test]), "|", colored("Passed","green"))