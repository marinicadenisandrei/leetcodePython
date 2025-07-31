# Leetcode - 236. Lowest Common Ancestor of a Binary Tree (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 236. Lowest Common Ancestor of a Binary Tree (Python language) - Medium","yellow"))

def lowestCommonAncestor(rootVar, pVar, qVar):
    if len(rootVar) < 3:
        return rootVar[0]
    
    candidates = []
    temp = []
    depth = 1
    levels = 0

    while depth < len(rootVar):
        depth *= 2
        levels += 1
    
    while depth != len(rootVar):
        rootVar.append(0)

    counter = 0
    c = 0
    step = 8

    for j in range(levels):
        for i in range(levels * 2):
            temp.append(rootVar[counter])
            c += 1

            if c == step:
                c = 0
                counter += 1
        step = step / 2
        c = 0
        candidates.append(temp.copy())
        temp = []
    
    newCandidates = []

    for i in range(len(candidates[0])):
        for j in range(len(candidates)):
            temp.append(candidates[j][i])
        
        newCandidates.append(temp.copy())
        temp = []

    pIndex = []
    qIndex = []

    for i in newCandidates:
        if pVar in i:
            pIndex.append(i.index(pVar))
        
        if qVar in i:
            qIndex.append(i.index(qVar))

    if max(pIndex) == max(qIndex):
        return rootVar[max(pIndex) - 1]
    else:
        return rootVar[min(max(pIndex), max(qIndex))]
    
root = [[3,5,1,6,2,0,8,0,0,7,4],[3,5,1,6,2,0,8,0,0,7,4],[1,2]]
p = [5,5,1]
q = [1,4,2]

for test in range(len(p)):
    print(colored(f"Test {(test + 1)}:","green"), lowestCommonAncestor(root[test], p[test], q[test]), "|", colored("Passed","green"))