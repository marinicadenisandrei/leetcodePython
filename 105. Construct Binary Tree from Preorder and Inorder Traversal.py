# Leetcode - 105. Construct Binary Tree from Preorder and Inorder Traversal (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 105. Construct Binary Tree from Preorder and Inorder Traversal (Python language) - Medium", "yellow"))

preorderTest = [[3,9,20,15,7], [-1]]
inorderTest = [[9,3,15,20,7], [-1]]

def makeRoot(list_var):
    new_list_var = []
    for i in list_var:
        if len(i) == 1 and i[0] not in new_list_var:
            new_list_var.append(i[0])
        elif len(i) == 0:
            new_list_var.append(0)
    
    return new_list_var

def removeLastZeros(list_var):
    for i in reversed(list_var):
        if i != 0:
            return list_var[:list_var.index(i) + 1]
        
for test in range(len(preorderTest)):
    preorder = preorderTest[test]
    inorder = inorderTest[test]

    output = [preorder[0]]

    left = [inorder[:inorder.index(preorder[0])]]
    right = [inorder[inorder.index(preorder[0]) + 1:]]

    for i in preorder[1:]:
        if i in left[-1]:
            left.append([i])
            left.append(left[-2][:left[-2].index(i)])
            left.append(left[-3][left[-3].index(i) + 1:])

        if i in right[-1]:
            right.append([i])
            right.append(right[-2][:right[-2].index(i)])
            right.append(right[-3][right[-3].index(i) + 1:])

    left = makeRoot(left)
    right = makeRoot(right)

    counter = 0

    while len(left) > 0 or len(right) > 0:
        output.extend(left[:pow(2,counter)].copy())
        output.extend(right[:pow(2,counter)].copy())

        left = left[pow(2,counter):]
        right = right[pow(2,counter):]

        counter += 1

    output = removeLastZeros(output)

    testNumber = test + 1

    print(colored(f"Test {testNumber}:", "green"), output, "|", colored("Passed", "green"))
