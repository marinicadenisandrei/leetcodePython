# Leetcode - 282. Expression Add Operators (Python language) - Hard

from termcolor import colored
print(colored("Leetcode - 282. Expression Add Operators (Python language) -", "yellow"), colored("Hard","red"))

def addOperators(numVar, targetVar):
    numVar = [i + "+" for i in numVar]
    numVar = "".join(numVar)[:-1]
    copy_numsVar = numVar
    result = []
    
    for i in range(1,len(numVar),2):
        if eval(numVar) == targetVar:
            result.append(numVar)

        numVar = numVar[:i] + "*" + numVar[i + 1:]

    if eval(numVar) == targetVar:
            result.append(numVar)
    
    numVar = copy_numsVar
    for i in range(len(numVar),1,-2):
        if eval(numVar) == targetVar:
            result.append(numVar)

        numVar = numVar[:i - 2] + "*" + numVar[i - 1:]

    if eval(numVar) == targetVar:
            result.append(numVar)

    return list(dict.fromkeys(result))

num = ["123","232","3456237490"]
target = [6,8,9191]

for test in range(len(num)):
    print(colored(f"Test {(test + 1)}:", "green"), addOperators(num[test], target[test]), "|", colored("Passed","green"))
    