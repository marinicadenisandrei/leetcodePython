# Leetcode - 140. Word Break II (Python language) - Hard

from termcolor import colored

print(colored("Leetcode - 140. Word Break II (Python language) - ", "yellow"), colored("Hard", "red"))

def wordBreak(sVar : str, wordDictVar : list):
    listIndex = []
    dictCopy = wordDictVar.copy()

    for i in wordDictVar:
        listIndex.append(sVar.find(i))

    flag = True

    while flag:
        flag = False

        for i in range(len(listIndex) - 1):
            if listIndex[i] > listIndex[i + 1]:
                listIndex[i], listIndex[i + 1] = listIndex[i + 1], listIndex[i]
                wordDictVar[i], wordDictVar[i + 1] = wordDictVar[i + 1], wordDictVar[i]
                flag = True
    
    target = sVar
    targetList = wordDictVar.copy()
    stringVar = ""
    result = []

    flag = True

    while flag:
        flag = False

        for i in targetList:
            if i[0] == target[0]:
                stringVar += i + " "
                wordDictVar.remove(i)
                target = target.replace(i, "", 1)
                flag = True

        if len(target) > 0:
            stringVar += target

        if stringVar[-1] == " ":
            result.append(stringVar[:-1])
        else:
            result.append(stringVar)

        stringVar = ""
        target = sVar
        targetList = wordDictVar.copy()
    
    temp = result[0].split(" ")

    stringVar = ""
    target = sVar

    for i in range(len(temp)):
        for j in range(len(temp) - 1):
            if j == i:
                stringVar += temp[j] + temp[j + 1] + " "
                target = target.replace(temp[j] + temp[j + 1], "", 1)
                temp.remove(temp[j + 1])
            else:
                target = target.replace(temp[j], "", 1)
        
                stringVar += temp[j] + " "
                target = target.replace(temp[j], "", 1)
        
        if stringVar.replace(" ","") == sVar:
            if stringVar[-1] == " ":
                result.append(stringVar[:-1])
            else:
                result.append(stringVar)

        temp = result[0].split(" ") 
        stringVar = ""
        target = sVar

    for i in result:
        if len(i.split(" ")) == 1:
            result.remove(i)
    
    flag = True

    while flag:
        flag = False
        for i in result:
            for j in i.split(" "):
                if j not in dictCopy:
                    result.remove(i)
                    flag = True
                    break
            
            if flag:
                break   

    result = list(dict.fromkeys(result))
    return result        

s = ["catsanddog", "pineapplepenapple"]
wordDict = ["cat","cats","and","sand","dog"], ["apple","pen","applepen","pine","pineapple"]

for test in range(len(s)):
    print(colored(f"Test {(test + 1)}:", "green"), wordBreak(s[test], wordDict[test]), "|", colored("Passed", "green"))