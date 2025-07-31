# Leetcode - 227. Basic Calculator II (Python language) - Medium

from termcolor import colored
print(colored("Leetcode - 227. Basic Calculator II (Python language) - Medium","yellow"))

def calculate(sVar):
    sVar = sVar.replace(" ","")

    while "*" in sVar or "/" in sVar:
        start = 0
        end = 0
        string1 = ""
        string2 = ""

        for i in range(len(sVar)):
            if sVar[i] == "*" or sVar[i] == "/":
                for j in range(i - 1,0,-1):
                    if sVar[j].isdigit():
                        string1 += sVar[j]
                        start = j
                    else:
                        break
                
                for j in range(i + 1,len(sVar)):
                    if sVar[j].isdigit():
                        string2 += sVar[j]
                        end = j
                    else:
                        break
                
                if len(string1) == 0:
                    string1 += sVar[0]
                    start = 0
                
                if sVar[i] == "*":
                    sVar = sVar[:start] + str(int(string1) * int(string2)) + sVar[end + 1:len(sVar)]
                elif sVar[i] == "/":
                    sVar = sVar[:start] + str(int(int(string1) / int(string2))) + sVar[end + 1:len(sVar)]
                break
    
    while "+" in sVar or "-" in sVar:
        start = 0
        end = 0
        string1 = ""
        string2 = ""

        for i in range(len(sVar)):
            if sVar[i] == "+" or sVar[i] == "-":
                for j in range(i - 1,0,-1):
                    if sVar[j].isdigit():
                        string1 += sVar[j]
                        start = j
                    else:
                        break
                
                for j in range(i + 1,len(sVar)):
                    if sVar[j].isdigit():
                        string2 += sVar[j]
                        end = j
                    else:
                        break
                
                if len(string1) == 0:
                    string1 += sVar[0]
                    start = 0
                
                if sVar[i] == "+":
                    sVar = sVar[:start] + str(int(string1) + int(string2)) + sVar[end + 1:len(sVar)]
                elif sVar[i] == "-":
                    sVar = sVar[:start] + str(int(string1) - int(string2)) + sVar[end + 1:len(sVar)]
                break
    
    return sVar
    
s = ["3+2*2"," 3/2 "," 3+5 / 2 "]

for test in range(len(s)):
    print(colored(f"Test {(test + 1)}:","green"), calculate(s[test]), "|", colored("Passed","green"))