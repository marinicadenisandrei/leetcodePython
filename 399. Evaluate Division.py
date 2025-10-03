# Leetcode - 399. Evaluate Division (Python language) - Medium */

from termcolor import colored

print(colored("Leetcode - 399. Evaluate Division (Python language) - Medium","yellow"))

def calcEquation(equationsVar, valuesVar, queriesVar):
    result = []

    for i in queriesVar:
        index1 = -1
        index2 = -1

        if i in equationsVar:
            idx = equationsVar.index(i)
            result.append(values[idx][0])
            continue
        elif i[::-1] in equationsVar:
            idx = equationsVar.index(i[::-1])
            result.append(1/valuesVar[idx])
            continue

        for ind in range(len(equationsVar)):
            if i[0] in equationsVar[ind] and index1 == -1:
                index1 = ind
            
            if i[1] in equationsVar[ind] and index2 == -1:
                index2 = ind
        
        if index1 == -1 or index2 == -1:
            result.append(-1)
        elif i[0] == i[1]:
            result.append(1)
            continue
        elif index1 != index2:
            result.append(valuesVar[index1] * valuesVar[index2])
        elif index1 == index2:
            if equationsVar[index1][0] == i[0]:
                result.append(valuesVar[index1])
            else:
                result.append(1/valuesVar[index1])
    
    return result

equations = [[["a","b"],["b","c"]],[["a","b"],["b","c"],["bc","cd"]],[["a","b"]]]
values = [[2.0,3.0],[1.5,2.5,5.0],[0.5]]
queries = [[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]],[["a","c"],["c","b"],["bc","cd"],["cd","bc"]],[["a","b"],["b","a"],["a","c"],["x","y"]]]

for test in range(len(values)):
    print(
        colored(f"Test {(test + 1)}:","green"),
        calcEquation(equations[test], values[test], queries[test]),
        "|",
        colored("Passed","green")
    )
    