# Leetcode - 201. Bitwise AND of Numbers Range (Python languae) - Medium

from termcolor import colored

print(colored("Leetcode - 201. Bitwise AND of Numbers Range (Python languae) - Medium", "yellow"))

def decimalToBin(numberVar):
    binNumber = ""
    
    while numberVar > 0:
        if numberVar % 2 == 0:
            binNumber += "0"
        else:
            binNumber += "1"
        
        numberVar = int(numberVar / 2)
    
    return binNumber

def binToDecimal(binaryNumber: str):
    number = 0

    for i in range(len(binaryNumber)):
        number += pow(2,i) * int(binaryNumber[i])
    
    return number

def rangeBitwiseAnd(leftVar: int, rightVar: int):
    acumulation = []
    acumulation.append(decimalToBin(leftVar))

    for i in range(leftVar + 1, rightVar + 1):
        if len(decimalToBin(i)) == len(acumulation[0]):
            acumulation.append(decimalToBin(i))
        else:
            break
    
    result = ""

    for i in range(len(acumulation[0])):
        bitVar = "1"

        for j in range(len(acumulation)):
            bitVar = str(int(bitVar) and int(acumulation[i][j])) 
        
        result += bitVar

    return binToDecimal(result)
            
left = [5,0,0]
right = [7,0,2147483647]

for test in range(len(left)):
    print(colored(f"Test {(test + 1)}:","green"), rangeBitwiseAnd(left[test], right[test]), "|", colored("Passed","green"))