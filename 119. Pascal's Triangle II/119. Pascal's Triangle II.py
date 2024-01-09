from termcolor import colored

print(colored("Leetcode - 119. Pascal's Triangle II (Python language) -", "yellow"), colored("Easy", "green"))

def getRow(rowIndexVar):
    acumulation = [[1], [1,1]]

    if rowIndexVar < 0:
        return -1

    if rowIndexVar < 2:
        return acumulation[rowIndexVar]

    for i in range(rowIndexVar - 1):
        acumulation.append([])
        acumulation[-1].append(1)

        for j in range(len(acumulation[-2]) - 1):
            acumulation[-1].append(acumulation[-2][j] + acumulation[-2][j + 1])
        
        acumulation[-1].append(1)
    
    return acumulation[-1]
    

rowIndex = [3,0,1]
for test in range(len(rowIndex)):
    testNumber = test + 1
    print(colored(f"Test {testNumber}:", "green"), getRow(rowIndex[test]), "|", colored("Passed", "green"))

