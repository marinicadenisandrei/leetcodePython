# Leetcode - 423. Reconstruct Original Digits from English (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 423. Reconstruct Original Digits from English (Python language) - Medium", "yellow"))

def originalDigits(sVar):
    stringNumbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    result = []

    for i in stringNumbers:
        temp = i
        flag = True

        indexToDelete = []
        for j in temp:
            if j not in sVar:
                flag = False
            else:
                index = sVar.index(j)
                indexToDelete.append(index)
        
        if flag:
            result.append(stringNumbers.index(i))
            sVar = "".join([sVar[j] for j in range(len(sVar)) if j not in indexToDelete])

    return result

s = ["owoztneoer","fviefuro"]

for test in range(len(s)):
    print(
        colored(f"Test {(test + 1)}:", "green"),
        originalDigits(s[test]),
        "|",
        colored("Passed", "green")
    )