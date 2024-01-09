# Leetcode - 101. Symmetric Tree (Python language) - Easy

from termcolor import colored

print(colored("Leetcode - 101. Symmetric Tree (Python language) -", "yellow"), colored("Easy", "green"))

rootTest = [[1,2,2,3,4,4,3,1,2,3,4,4,3,2,1], [1,2,2,0,3,0,3]]

def depth(number_len):
    n = 1

    while number_len > 0:
        number_len -= pow(2,n)
        n += 1
    
    return n - 2

for test in range(len(rootTest)):
    root = rootTest[test]
    n = 1
    flag = True

    for i in range(depth(len(root))):
        temp = root[pow(2, n) - 1 : pow(2, n + 1) - 1]

        if temp[0:int(len(temp)/2)].sort() != temp[int(len(temp)/2):].sort() or 0 in temp:
            flag = False

        n += 1

    testNumber = test + 1

    print(colored(f"Test {testNumber}:", "green"), flag, "|", colored("Passed", "green"))
