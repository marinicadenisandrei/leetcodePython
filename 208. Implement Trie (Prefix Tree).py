# Leetcode - 208. Implement Trie (Prefix Tree) (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 208. Implement Trie (Prefix Tree) (Python language) - Medium","yellow"))

def Trie(methodsVar: list, elementsVar: list):
    acumulation = []
    results = ["null"]

    for i in range(1,len(methodsVar)):
        if methodsVar[i] == "insert":
            acumulation.append(elementsVar[i][0])
            results.append("null")
        elif methodsVar[i] == "search":
            if elementsVar[i][0] in acumulation:
                results.append(True)
            else:
                results.append(False)
        elif methodsVar[i] == "startsWith":
            flag = False

            for j in acumulation:
                if j[:len(elementsVar[i][0])] == elementsVar[i][0]:
                    results.append(True)
                    flag = True
                    break
            
            if not flag: results.append(False)
    
    return results
                
methods = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
elements = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
print(colored("Test 1:","green"), Trie(methods, elements), "|", colored("Passed","green"))