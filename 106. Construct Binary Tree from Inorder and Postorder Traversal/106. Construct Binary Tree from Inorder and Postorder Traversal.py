# Leetcode - 106. Construct Binary Tree from Inorder and Postorder Traversal (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 106. Construct Binary Tree from Inorder and Postorder Traversal (Python language) - Medium", "yellow"))

def makeLists(listVar):
    new = []

    for i in listVar:
        if len(i) == 1 and i[0] not in new:
            new.append(i[0])
        elif len(i) == 0:
            new.append(0)
    
    return new

inorderTest = [[9,3,15,20,7], [-1]]
postorderTest = [[9,15,7,20,3], [-1]]

for test in range(len(inorderTest)):
    inorder = inorderTest[test]
    postorder = postorderTest[test]
    
    output = [postorder[-1]]

    if len(inorder) > 1:
        left = [inorder[:inorder.index(output[0])]]
        right = [inorder[inorder.index(output[0]) + 1:]]

        for i in reversed(postorder[:-1]):
            if i in left[-1] and len(left[-1]) > 0:
                left.append([i])
                left.append(left[-2][:left[-2].index(i)])
                left.append(left[-3][left[-3].index(i) + 1:])

            if i in right[-1] and len(right[-1]) > 1:
                right.append([i])
                right.append(right[-2][:right[-2].index(i)])
                right.append(right[-3][right[-3].index(i) + 1:])

        left = makeLists(left)
        right = makeLists(right)
                
        counter = 0

        while len(left) > 0 and len(right) > 0:
            output.extend(left[:pow(2,counter)])
            output.extend(right[:pow(2,counter)])

            left = left[pow(2,counter):]
            right = right[pow(2,counter):]

            counter += 1

    testNumber = test + 1

    print(colored(f"Test {testNumber}:", "green"), output, "|", colored("Passed", "green"))