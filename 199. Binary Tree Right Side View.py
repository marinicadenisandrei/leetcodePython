# Leetcode - 199. Binary Tree Right Side View (Python language) - Medium

from termcolor import colored
print(colored("Leetcode - 199. Binary Tree Right Side View (Python language) - Medium","yellow"))

def rightSideView(rootVar: list):
    if len(rootVar) == 0:
        return []
        
    result = []
    power = 2
    result.append(rootVar[0])
    rootVar.pop(0)

    while len(rootVar) > 0:
        result.append(rootVar[:power][-1])
        rootVar = rootVar[power:]
        power *= 2
    
    return result


root = [[1,2,3,0,5,0,4],[1,0,3],[]]

for test in range(len(root)):
    print(colored(f"Test {(test + 1)}:","green"), rightSideView(root[test]), "|", colored("Passed","green"))