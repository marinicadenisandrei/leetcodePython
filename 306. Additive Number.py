# Leetcode - 306. Additive Number (Python language) - Medium 

from termcolor import colored

print(colored("Leetcode - 306. Additive Number (Python language) - Medium","yellow"))

def isAdditiveNumber(numVar):
    cutVar = numVar[0]

    for j in range(1,len(numVar)):
        flag = True

        for i in range(1,len(numVar) - j - 2):
            temp = numVar[len(cutVar):len(cutVar) + j]
            temp = int(temp) + int(cutVar)
            
            if numVar.find(str(temp)) != -1 and numVar.find(str(temp)) == j + 1:
                numVar = numVar[j + 1:]
                cutVar = str(temp)
            else:
                flag = False
                break
                
            j = len(cutVar)   

            if j * 2 == len(numVar):
                break
        
        if flag:
            return True

    return False
            

        
    
num = ["112358","199100199"]

for test in range(len(num)):
    print(colored(f"Test {(test + 1)}:","green"), isAdditiveNumber(num[test]), "|", colored("Passed","green"))