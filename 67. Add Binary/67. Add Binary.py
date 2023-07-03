# Leetcode - 67. Add Binary (Python language)

from termcolor import colored

print(colored("Leetcode - 67. Add Binary (Python language)", "yellow"))

state = colored("Passed", "green")

a = ["11","1010"]
b = ["1","1011"]

def BinaryToDecimal(decimalNumber : str):
    number = 0
    power = 0

    for i in decimalNumber[::-1]:
        if i == "1":
            number += 2**power
        
        power += 1

    return number

def decimalToBinary(firstNumber, secondNumber : str):
    firstNumber = int(firstNumber) + int(secondNumber)
    binaryNumber = ""

    while(firstNumber > 0):
        
        if str(firstNumber/2).split(".")[1] == "0":
            binaryNumber += "0"
        else:
            binaryNumber += "1"

        firstNumber = int(firstNumber/2)

    return binaryNumber[::-1]


for i in range(len(a)):
    testNumber = i+1
    text = colored(f"Test {testNumber}: ","green")
    result = decimalToBinary(str(BinaryToDecimal(a[i])),str(BinaryToDecimal(b[i])))
    print(f"{text}{result} | {state}")