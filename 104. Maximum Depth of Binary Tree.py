from termcolor import colored

print(colored("Leetcode - 104. Maximum Depth of Binary Tree -", "yellow"), colored("Easy", "green"))

rootTest = [[3,9,20,0,0,15,7], [1,0,2]]

def binarySearchTreeDepth(len_list):
    counter = 0

    while len_list > 0:
        len_list -= pow(2, counter)
        counter += 1

    return counter


for test in range(len(rootTest)):
    root = rootTest[test]

    testNumber = test + 1
    print(colored(f"Test {testNumber}:", "green"), binarySearchTreeDepth(len(root)), "|", colored("Passed", "green"))
