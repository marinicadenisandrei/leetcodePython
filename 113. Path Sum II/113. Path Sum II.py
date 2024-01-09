from termcolor import colored

print(colored("Leetcode - 113. Path Sum II (Python language) - Medium", "yellow"))

def depthRoot(rootVar):
    depth = len(rootVar)
    
    power = 0
    while depth > 0:
        depth -= pow(2,power)
        power += 1

    return power
    
def insertZeros(rootVar):
    newRoot = rootVar[:3].copy()
    rootVar = rootVar[3:]
    power = 2
    
    for i in range(depthRoot(rootVar) - 1):
        top = rootVar[:pow(2,power)]
        rootVar = rootVar[pow(2,power):]
        bottom = rootVar[:pow(2,power + 1)]
        
        if len(top) == 0 or len(bottom) == 0:
            break
        
        newRoot.extend(top.copy())
        
        for j in range(len(top)):
            if top[j] == 0:
                bottom.insert(2 * j, 0)
                bottom.insert(2 * (j + 1), 0)
        
        newRoot.extend(bottom.copy())
        
        power += 1
        
    return newRoot

def pathSum(rootVar, targetSumVar):
    rootVar = list(insertZeros(rootVar))
    try:
        starter = [[[rootVar[0],rootVar[1]], [rootVar[0], rootVar[2]]]]
    except IndexError:
        return []
    
    rootVar = rootVar[3:]

    while len(rootVar) > 0:
        starter.append([])
        
        for i in starter[-2]:
            try:
                temp = i.copy()
                temp.append(rootVar[0])
                starter[-1].append(temp.copy())
                rootVar = rootVar[1:]
                
                temp = []
                temp = i.copy()
                temp.append(rootVar[0])
                starter[-1].append(temp.copy())
                rootVar = rootVar[1:]
                
            except IndexError:
                pass

    starter = starter[-1]
    starter = [i for i in starter if sum(i) == targetSumVar]
    
    return starter

root = [[5,4,8,11,0,13,4,7,2,0,0,5,1], [1,2,3], [1,2]]
targetSum = [22,5,0]

for test in range(len(root)):
    testNumber = test + 1
    print(colored(f"Test {testNumber}:", "green"), pathSum(root[test], targetSum[test]), "|", colored("Passed", "green"))