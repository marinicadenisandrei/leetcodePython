from termcolor import colored

print(colored("Leetcode - 115. Distinct Subsequences (Python language) -", "yellow"), colored("Hard", "red"))

def ascendingElements(listVar):
    for i in range(1,len(listVar)):
        if listVar[i-1] > listVar[i]:
            return False
    
    return True

def createAcumulation(s, t):
    output = []
    
    for i in t:
        temp = [_ for _ in range(len(s)) if s[_] == i]
        output.append(temp.copy())
        temp.clear()
        
    return output

def removeDuplicatesLists(listVar):
    unique_set = set()
    unique_list = [sublist for sublist in listVar if tuple(sublist) not in unique_set and not unique_set.add(tuple(sublist))]
    
    return unique_list

def numDistinct(s, t):
    acumulation = createAcumulation(s, t)
    outputResult = [[]]
    
    for i in acumulation[0]:
        for j in acumulation[1]:
            outputResult[0].append([i,j])
    
    acumulation = removeDuplicatesLists(acumulation)
    acumulation = acumulation[2:]
    
    while len(acumulation) > 0:
        outputResult.append([])
        for j in acumulation[0]:
            for i in outputResult[-2]:
                formation = list(i.copy())
                formation.append(j)
                outputResult[-1].append(formation.copy())
                formation.clear()
        
        outputResult = outputResult[1:]
        acumulation = acumulation[1:]
    
    counter = 0
    
    for i in outputResult[0]:
        if ascendingElements(i):
            counter += 1
            
    return counter

s = ["rabbbit", "babgbag"] 
t = ["rabbit", "bag"]

for test in range(len(s)):
    result = numDistinct(s[test], t[test])
    testNumber = test + 1
    print(colored(f"Test {testNumber}:", "green"), result, "|", colored("Passed", "green"))