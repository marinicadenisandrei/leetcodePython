# Leetcode - 93. Restore IP Addresses (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 93. Restore IP Addresses (Python language) - Medium", "yellow"))

############################################## FUNCTIONS ##############################################

def validate_depth(listVar, depthVar):
    for i in listVar[:depthVar]:
        if len(str(i)) < 3:
            return False
    
    return True

def validIpAddress(listVar):
    for i in range(len(listVar)):
        integerVar = int(listVar[i])
        if (integerVar < 0 or integerVar > 255) or (len(listVar[i]) > 1 and listVar[i][0] == "0") or (len(listVar[i]) > 3):
            return False
    
    return True

########################################################################################################

sTest = ["25525511135", "0000", "101023"]

for test in range(len(sTest)):
    s = sTest[test]

    s_size = len(s)

    output = []

    structure = ["1", "1", "1", str(len(s)-3)]

    depth = 0
    IP_SIZE = 4

    while s_size > IP_SIZE - depth or s_size < 3:
        s_size -= 3
        depth += 1

        if s_size < 3:
            break

    if depth == 0:
        output = [s[i] + "." if i < 3 else s[i] for i in range(len(s))]
    else:
        model = []
        counter = 0

        model.append(structure)
        counter = 0

        while counter < depth:
            if "3" not in structure:
                factor = 2
            elif int(max(structure)) > 2:
                factor = 3

            if factor == 3:
                for i in range(len(structure)):
                    if int(structure[i]) >= factor:
                        structure[i-1] = str(int(structure[i-1]) + 1)
                        structure[i] = str(int(structure[i]) - 1)
                        break
            elif factor == 2:
                for i in range(len(structure)-1,0,-1):
                    if int(structure[i]) >= factor:
                        structure[i-1] = str(int(structure[i-1]) + 1)
                        structure[i] = str(int(structure[i]) - 1)
                        break
                
            if structure[0] == "3":
                structure = structure[1:]
                counter += 1

            if len(structure) == IP_SIZE:
                model.append(structure.copy())
            else:
                temp = ["3" for _ in range(IP_SIZE - len(structure))]
                temp.extend(structure.copy())
                model.append(temp)
                temp = []


        s_copy = s

        for i in range(len(model)):
            temp = []
            string_temp = ""

            string_temp = s[:int(model[i][0])]
            s = s[int(model[i][0]):]
            temp.append(string_temp)

            for j in range(1,len(model[i])):
                string_temp = s[:(int(model[i][j]))]
                s = s[(int(model[i][j])):]
                temp.append(string_temp)

            if validIpAddress(temp):
                output.append(temp.copy())
            
            s = s_copy

    testNumber = test + 1

    print(colored(f"Test {testNumber}:", "green"), output, "|", colored("Passed", "green"))





