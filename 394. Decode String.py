# Leetcode - 394. Decode String (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 394. Decode String (Python language) - Medium","yellow"))

def decodeString(sVar):
    flag = True

    while flag:
        flag = False
        indexFirst = sVar.rfind("[")
        indexLast = sVar.find("]")

        if indexFirst > indexLast:
            indexFirst = sVar.find("[")
            
        if indexFirst == -1 or indexLast == -1:
            break
        else:
            temp = str(int(sVar[indexFirst - 1]) * sVar[indexFirst + 1 : indexLast])
            sVar = sVar[:indexFirst - 1] + temp + sVar[indexLast + 1:]
            flag = True
        
    return sVar
        
s = ["3[a]2[bc]","3[a2[c]]","2[abc]3[cd]ef"]

for test in range(len(s)):
    print(
        colored(f"Test {(test + 1)}:","green"),
        decodeString(s[test]),
        "|",
        colored("Passed","green")
    )