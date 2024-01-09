# Leetcode - 118. Pascal's Triangle (Python language) - Easy

from termcolor import colored

print(colored("Leetcode - 118. Pascal's Triangle (Python language) -","yellow"), colored("Easy","green"))

def generate(numRows):
    output = [[1], [1,1]]

    if numRows == 1:
        return output[0]
    elif numRows == 2:
        return output[1]
        
    for i in range(numRows - 2):
        output.append([1])
        for j in range(1,len(output[-2])):
            output[-1].append(output[-2][j-1] + output[-2][j])
        
        output[-1].append(1)
    
    return output

numRows = [5,1]
for test in range(len(numRows)):
    testNumber = test + 1
    print(colored(f"Test {testNumber}:","green"),generate(numRows[test]),"|",colored("Passed","green"))
