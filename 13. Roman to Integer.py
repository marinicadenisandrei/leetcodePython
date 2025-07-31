# Leetcode - 12. Integer to Roman (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 12. Integer to Roman (Python language) - Medium", "yellow"))

database = {
    "I" : 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
} 

sTest = ["III", "LVIII", "MCMXCIV"]

for test in range(len(sTest)):
    s = sTest[test]

    numberListFormation = []

    for i in s:
        numberListFormation.append(database[str(i)])

    number = 0
    factor = 1

    while len(numberListFormation) > 1:
        if numberListFormation[0] < numberListFormation[1]:
            number += (numberListFormation[1] - numberListFormation[0])
            numberListFormation = numberListFormation[2:]
        else:
            number += numberListFormation[0]
            numberListFormation = numberListFormation[1:]

    if len(numberListFormation) == 1:
        number += numberListFormation[0]

    testNumber = test + 1

    print(colored(f"Test {testNumber}:","green"), number, "|", colored("Passed","green"))
