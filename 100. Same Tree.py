# Leetcode - 100. Same Tree (Python language) - Easy

from termcolor import colored

print(colored("Leetcode - 100. Same Tree (Python language) -", "yellow"), colored("Easy", "green"))

pTest = [[1, 2, 3], [1,2]]
qTest = [[1, 2, 3], [1,0,2]]

for test in range(len(pTest)):
    p = pTest[test]
    q = qTest[test]
    
    x = lambda list1, list2 : all(list1[i] == list2[i] for i in range(len(list1)))

    result = x(p, q)
    testNumber = test + 1
    
    print(colored(f"Test {testNumber}:", "green"), result, "|", colored("Passed", "green"))