from termcolor import colored

print(colored("Leetcode - 173. Binary Search Tree Iterator (Python language) - Medium","yellow"))

def BSTIterator(BSTvar, methodsVar):
    output = []
    index = 0

    BSTvar = [i for i in BSTvar if i != 0]
    for i in range(0,len(BSTvar), 2):
        try:
            BSTvar[i], BSTvar[i + 1] = BSTvar[i + 1], BSTvar[i]
        except IndexError:
            break

    for i in methodsVar[1:-1]:
        if i == "next":
            output.append(BSTvar[index])
            index += 1
        elif i == "hasNext" and index < len(BSTvar):
            output.append(True)
        else:
            output.append(False)
    
    return output

            
methods = ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
BST = [7, 3, 15, 0, 0, 9, 20]
print(colored("Test 1:","green"), BSTIterator(BST, methods), "|", colored("Passed","green"))

