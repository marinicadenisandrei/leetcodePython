# Leetcode - 150. Evaluate Reverse Polish Notation (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 150. Evaluate Reverse Polish Notation (Python language) - Medium", "yellow"))

def evalRPN(tokensVar: list):
    flag = True

    while flag:
        flag = False

        for i in range(len(tokensVar)):
            try:
                float(tokensVar[i])
            except ValueError:
                exprVar = tokensVar[i - 2] + tokensVar[i] + tokensVar[i - 1]
                tokensVar[i - 2] = str(int(eval(exprVar)))
                tokensVar = tokensVar[:i - 1] + tokensVar[i + 1:]
                flag = True
                break

    return tokensVar[0] 
            
tokens = [["2","1","+","3","*"],["4","13","5","/","+"],["10","6","9","3","+","-11","*","/","*","17","+","5","+"]]

for test in range(len(tokens)):
    print(colored(f"Test {(test + 1)}:", "green"), evalRPN(tokens[test]), "|", colored("Passed", "green"))