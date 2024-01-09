from termcolor import colored

print(colored("Leetcode - 112. Path Sum (Python language) -", "yellow"),colored("Easy", "green"))

def checkForElement(listVar, element):
    for i in listVar:
        if i == element:
            return True
    
    return False

def depthBinTree(listVar):
    numberOfElements = len(listVar)
    power = 0

    while numberOfElements > 0:
        numberOfElements -= pow(2,power)
        power += 1
    
    return power    
        
def hasPathSum(listVar, targetSum):
    listVar[1] = listVar[0] + listVar[1]
    listVar[2] = listVar[0] + listVar[2]
    listVar = listVar[1:]

    if len(listVar) > 3:
        power = 1

        for i in range(depthBinTree(listVar) - 1):
            top = listVar[:pow(2,power)].copy()
            listVar = listVar[pow(2,power):]
            bottom = listVar[:pow(2,power + 1)].copy()
            index = -1

            needZero = []

            for k in range(len(bottom)):
                if bottom[k] == 0:
                    needZero.append(k)

            for k in needZero:
                listVar.insert(len(bottom) + k + 1, 0)
                listVar.insert(len(bottom) + k + 2, 0)

            for j in range(pow(2,power + 1)):
                if j % 2 == 0:
                    index += 1;
                
                listVar[j] = listVar[j] + top[index]

            power += 1
            needZero.clear()
    
    return checkForElement(listVar, targetSum)

root = [[5,4,8,11,0,13,4,7,2,0,0,0,1], [1,2,3]] 
targetSum = [22,5]

for test in range(len(root)):
    testNumber = test + 1
    print(colored(f"Test {testNumber}:", "green"), hasPathSum(root[test], targetSum[test]), "|", colored("Passed", "green"))
    





    



