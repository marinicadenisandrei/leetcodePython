# Leetcode - 224. Basic Calculator (Python language) - Hard

from termcolor import colored
print(colored("Leetcode - 224. Basic Calculator (Python language) -","yellow"), colored("Hard","red"))

def calculate(sVar: str):
    sVar = sVar.replace(" ","")
    
    if "(" not in sVar:
        sVar = "(" + sVar + ")"

    first = 0
    last = 0
    flag = True

    while "(" in sVar:
        calculation = 0

        for i in range(len(sVar)):
            if sVar[i] == "(":
                first = i
        
        for i in range(len(sVar) - 1,-1,-1):
            if sVar[i] == ")" and i > first:
                last = i
        
        
        elementFormation = ""
        indexStart = 0
        for i in range(first + 1, last):
            if sVar[i].isdigit():
                elementFormation += sVar[i]
            else:
                indexStart = i + 1
                break

        calculation = int(elementFormation)

        while indexStart < last:
            elementFormation = ""

            for i in range(indexStart, last):
                if sVar[i].isdigit():
                    elementFormation += sVar[i]
                else:
                    break
            
            if sVar[indexStart - 1] == "+":
                calculation += int(elementFormation)
            elif sVar[indexStart - 1] == "-":
                calculation -= int(elementFormation) 
                
            indexStart += len(elementFormation) + 1
        
        sVar = sVar[0:first] + str(calculation) + sVar[last + 1:len(sVar)]

        if "(" not in sVar and flag:
            sVar = "(" + sVar + ")"
            flag = False

    return int(sVar)

s = ["1 + 1", " 2-1 + 2 ", "(1+(4+5+2)-3)+(6+8)"]

for test in range(len(s)):
    print(colored(f"Test {(test + 1)}:","green"), calculate(s[test]), "|", colored("Passed"))