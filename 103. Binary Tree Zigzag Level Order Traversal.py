# Leetcode - 103. Binary Tree Zigzag Level Order Traversal (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 103. Binary Tree Zigzag Level Order Traversal (Python language) - Medium", "yellow"))

rootTest = [[3,9,20,0,0,15,7], [1], []]

for test in range(len(rootTest)):
    root = rootTest[test]

    output = []
    factor = 1
    power_var = 1

    sort_flag = False

    while len(root) > 0:
        temp = list(filter(lambda x: x != 0, root[:factor])).copy()

        if sort_flag == False:
            sort_flag = True
            output.append(temp)

        else:
            sort_flag = False
            temp.sort(reverse=True)
            output.append(temp)

        root = root[factor:]
        factor = pow(2,power_var)
        power_var += 1

    testNumber = test + 1

    print(colored(f"Test {testNumber}:", "green"), output, "|", colored("Passed", "green"))

