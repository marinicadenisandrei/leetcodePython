# Leetcode - 89. Gray Code (Python Language) - Medium

from termcolor import colored

print(colored("Leetcode - 89. Gray Code (Python Language) - Medium", "yellow"))

nTest = [2,1]

for test in range(len(nTest)):
    n = nTest[test]

    powerNumber = pow(2,n)

    integerList = [_ for _ in range(powerNumber)]
    copyIntegerList = integerList.copy()

    def integerToBinary(integer):
        binaryString = ""

        while integer > 0:
            if integer % 2 == 0:
                binaryString = "0" + binaryString
            else:
                binaryString = "1" + binaryString
        
            integer = int(integer / 2)

        return binaryString


    for i in range(len(integerList)):
        integerList[i] = integerToBinary(integerList[i])
        lengthBinary = len(integerList[i])

        if lengthBinary < n:
            integerList[i] = "0" * (n - lengthBinary) + integerList[i]


    integerList = [''.join(sorted(_)) for _ in integerList]

    flag = True

    while flag:
        flag = False

        for i in range(0,len(integerList)):
            if integerList[i-1] == integerList[i]:
                integerList[i], integerList[i+1] = integerList[i+1], integerList[i]
                copyIntegerList[i], copyIntegerList[i+1] = copyIntegerList[i+1], copyIntegerList[i]

                flag = True
                break

    testNumber = test + 1

    print(colored(f"Test {testNumber}:", "green"), copyIntegerList, "|", colored("Passed", "green"))




