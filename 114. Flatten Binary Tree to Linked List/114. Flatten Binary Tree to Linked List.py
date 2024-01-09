from termcolor import colored

print(colored("Leetcode - 114. Flatten Binary Tree to Linked List (Python) - Medium", "yellow"))

def flatten(rootVar):
    if len(rootVar) == 1 and rootVar[0] == 0:
        return [0];
    
    flattened = [item for i in rootVar if i != 0 for item in (i, 0)]
    flattened = flattened[:-1]

    return flattened

root = [[1,2,5,3,4,0,6],[],[0]]

for test in range(len(root)):
    root[test] = flatten(root[test])
    testNumber = test + 1

    print(colored(f"Test {testNumber}:","green"), root[test], "|", colored("Passed", "green"))