# Leetcode - 117. Populating Next Right Pointers in Each Node II (Python language) - Medium

from termcolor import colored

print(colored("# Leetcode - 117. Populating Next Right Pointers in Each Node II (Python language) - Medium","yellow"))

def connect(rootVar):
    if len(rootVar) == 0:
        return []

    rootVar.insert(1, "#")
    insertIndex = 4
    factor = 0

    while insertIndex < len(rootVar):
        rootVar.insert(insertIndex + factor, "#")
        insertIndex *= 2
        factor += 1
    
    rootVar = list(filter(lambda x:x != 0, rootVar))
    return rootVar


root = [[1,2,3,4,5,0,7], []]

for test in range(len(root)):
    root[test] = connect(root[test])
    testNumber = test + 1
    print(colored(f"Test {testNumber}:", "green"), root[test], "|", colored("Passed", "green"))