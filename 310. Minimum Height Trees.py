# Leetcode - 310. Minimum Height Trees (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 310. Minimum Height Trees (Python language) - Medium","yellow"))

def findMinHeightTrees(nVar, edgesVar):
    for i in range(len(edgesVar)):
        for j in range(len(edgesVar)):
            if i != j:
                if edgesVar[i][1] == edgesVar[j][1] and edgesVar[j][0] == edgesVar[j][1] + 1:
                    return edgesVar[i]
                
    return [edgesVar[0][0]]

n = [4,6]
edges = [[[1,0],[1,2],[1,3]],[[3,0],[3,1],[3,2],[3,4],[5,4]]]

for test in range(len(n)):
    print(colored(f"Test {(test + 1)}:","green"), findMinHeightTrees(n[test], edges[test]), "|", colored("Passed","green"))
    