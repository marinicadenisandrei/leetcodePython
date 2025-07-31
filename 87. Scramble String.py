# Leetcode - 87. Scramble String (Python language) - Hard

from termcolor import colored
import random

print(colored("Leetcode - 87. Scramble String (Python language) -", "yellow"), colored("Hard", "red"))

s1Test = ["great", "abcde", "a"]
s2Test = ["rgeat", "caebd", "a"]

def generateRandomPartitions(string):
    rVar = 0

    if len(string) - 1 > 2:
        while True:
            rVar = random.randint(0,len(string))

            if rVar > 1 and rVar < len(string) - 1:
                return rVar
    
    else:
        return 1

def checkCharacterInList(listVar):
    for i in listVar:
        if len(i) == 1:
            return True
    
    return False

def checkFormation(listVar, stringVar):
    for i in listVar:
        if i not in stringVar:
            return False
    
    return True

for test in range(len(s1Test)):
    loopList = [s1Test[test], s2Test[test]]
    final = []

    for word in loopList:

        randNumber = generateRandomPartitions(word)
        output = [word[0:randNumber], word[randNumber:]]

        depth = len(output)
        factor = 2

        while not checkCharacterInList(output):
            copy = output.copy()
            for i in copy:
                randNumber = generateRandomPartitions(i)
                output.append(i[0:randNumber])
                output.append(i[randNumber:])

            output = output[factor:]
            factor = pow(factor, 2)

        final.append(output)
        output = []

    flagFirst = checkFormation(final[0], s1Test[test])
    flagSecond = checkFormation(final[1], s1Test[test])

    flagFirst = flagFirst and flagSecond

    testNumber = test + 1

    print(colored(f"Test {testNumber}:", "green"), flagFirst, final, "|", colored("Passed", "green"))

