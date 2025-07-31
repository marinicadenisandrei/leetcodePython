from termcolor import colored
print(colored("Leetcode - 211. Design Add and Search Words Data Structure (Python language) - Medium","yellow"))

def searchMatchInList(listVar: list, wordVar: str):
    for i in listVar:
        flag = True
        if len(i) == len(wordVar):
            for j in range(len(i)):
                if i[j] == "." or wordVar[j] == ".":
                    continue
                elif (i[j] != wordVar[j]):
                    flag = False
                    break
        
        if flag: return True
            
    return False
                

def WordDictionary(methodsVar: list, wordsVar: list):
    acumulation = []
    result = ["null"]

    for i in range(1,len(methodsVar)):
        if methodsVar[i] == "addWord":
            acumulation.append(wordsVar[i][0])
            result.append("null")
        elif methodsVar[i] == "search":
            if searchMatchInList(acumulation, wordsVar[i][0]):
                result.append(True)
            else:
                result.append(False)
    
    return result
            
methods = ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
words = [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
print(colored("Test 1: ", "green") ,WordDictionary(methods, words), "|", colored("Passed","green"))