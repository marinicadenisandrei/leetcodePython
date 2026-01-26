# Leetcode - 415. Add Strings (Python language) - Easy

from termcolor import colored

print(colored("Leetcode - 415. Add Strings (Python language) -", "yellow"), colored("Easy","green"))

def addStrings(num1Var, num2Var):
    return str(int(num1Var) + int(num2Var))

num1 = ["11","456","0"]
num2 = ["123","77","0"]

for test in range(len(num1)):
    print(
        colored(f"Test {test + 1}:","green"),
        addStrings(num1[test], num2[test]),
        "|",
        colored("Passed","green")
    )