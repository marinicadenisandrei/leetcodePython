# Leetcode - 357. Count Numbers with Unique Digits (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 357. Count Numbers with Unique Digits (Python language) - Medium", "yellow"))

def countNumbersWithUniqueDigits(nVar):
    starter = 0
    counter = 0

    while starter < 10 ** nVar:
        strNumber = str(starter)

        if len(set(strNumber)) == len(strNumber):
            counter += 1

        starter += 1

    return counter

n = [2,0]

for test in range(len(n)):
    print(colored(f"Test {(test + 1)}:","green"), countNumbersWithUniqueDigits(n[test]), "|", colored("Passed","green"))
