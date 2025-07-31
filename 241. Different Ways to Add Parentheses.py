# Leetcode - 241. Different Ways to Add Parentheses (Python language) - Medium

import warnings
from termcolor import colored

print(colored("Leetcode - 241. Different Ways to Add Parentheses (Python language) - Medium","yellow"))

warnings.filterwarnings("ignore", category=SyntaxWarning)

def diffWaysToCompute(expressionVar):
    counter = 0
    result = []
    copyExpr = expressionVar

    for i in ["*", "-", "+", "/"]:
        counter += expressionVar.count(i)

    expressionVar = "(" * counter + ")" * counter + expressionVar

    for i in range((counter * 2) - 1, 0, -1):
        for j in range(i, len(expressionVar) - 1):
            expressionVar = list(expressionVar)
            expressionVar[j], expressionVar[j + 1] = expressionVar[j + 1], expressionVar[j]
            expressionVar = ''.join(expressionVar)
            result.append(expressionVar)
    
    expressionVar = copyExpr
    expressionVar += ("(" * counter) + (")" * counter)

    for i in range(len(expressionVar) - (counter * 2), len(expressionVar) - 1):
        for j in range(i, 0, -1):
            expressionVar = list(expressionVar)
            expressionVar[j], expressionVar[j - 1] = expressionVar[j - 1], expressionVar[j]
            expressionVar = ''.join(expressionVar)
            result.append(expressionVar)

    expressionVar = copyExpr
    expressionVar = "(" * 3 + expressionVar + ")" * 3

    index1 = counter - 1
    index2 = len(expressionVar) - counter - 1

    while index1 < index2:
        expressionVar = list(expressionVar)
        expressionVar[index1], expressionVar[index1 + 1] = expressionVar[index1 + 1], expressionVar[index1]
        expressionVar = ''.join(expressionVar)
        result.append(expressionVar)

        expressionVar = list(expressionVar)
        expressionVar[index2], expressionVar[index2 + 1] = expressionVar[index2 + 1], expressionVar[index2]
        expressionVar = ''.join(expressionVar)
        result.append(expressionVar)

        index1 += 1
        index2 -= 1

    result = list(dict.fromkeys(result))
    numbersVar = []

    for i in result:
        try:
            if eval(i) not in numbersVar:
                numbersVar.append(eval(i))
                
        except (SyntaxError, TypeError) as e:
            continue
    
    return numbersVar

expression = ["2-1-1", "2*3-4*5"]
              
for test in range(len(expression)):
    print(colored(f"Test {(test + 1)}:", "green"), diffWaysToCompute(expression[test]), "|", colored("Passed", "green"))
