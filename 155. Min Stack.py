# Leetcode - 155. Min Stack (Python language) - Medium

from termcolor import colored
print(colored("Leetcode - 155. Min Stack (Python language) - Medium", "yellow"))

def minStack(methodsVar:list, elementsVar:list):
    stack = []
    acumulation = []
    for i in range(1,len(methodsVar)):
        if methodsVar[i] == "push":
            acumulation.append(elementsVar[i][0])
            stack.append("null")
        elif methodsVar[i] == "getMin":
            stack.append(min(acumulation))
        elif methodsVar[i] == "pop":
            acumulation.pop()
            stack.append("null")
        elif methodsVar[i] == "top":
            stack.append(acumulation[-1])
        
    return stack

methods = ["MinStack","push","push","push","getMin","pop","top","getMin"]
elements = [[],[-2],[0],[-3],[],[],[],[]]
print(colored("Test 1:", "green"),minStack(methods,elements),"|",colored("Passed","green"))