# Leetcode - 429. N-ary Tree Level Order Traversal (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 429. N-ary Tree Level Order Traversal (Python language) - Medium", "yellow"))

def levelOrder(rootVar):
    result = []
    acumulation = [[]]

    for i in range(len(rootVar)):
        if rootVar[i] != 0:
            acumulation[-1].append(rootVar[i])
        else:
            acumulation.append([])

    result.append(acumulation[0])
    result.append(acumulation[1])

    start = 2

    while start < len(acumulation):
        end = min(start + len(result[-1]), len(acumulation))
        unionCandidates = acumulation[start:end]
        temp = [x for sub in unionCandidates for x in sub]

        if temp:  
            result.append(temp)

        start = end

    return result


root = [[1,0,3,2,4,0,5,6],[1,0,2,3,4,5,0,0,6,7,0,8,0,9,10,0,0,11,0,12,0,13,0,0,14]]

for test in range(len(root)):
    print(colored(f"Test {(test + 1)}:","green"),
          levelOrder(root[test]),
          "|",
          colored("Passed","green"))
    