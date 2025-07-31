# Leetcode - 168. Excel Sheet Column Title (Python language) - Easy

from termcolor import colored

print(colored("Leetcode - 168. Excel Sheet Column Title (Python language) -", "yellow"), colored("Passed", "green"))

def convertToTile(columnNumberVar):
    if columnNumberVar <= 26:
        return DATABASE[columnNumberVar - 1]
        
    listVar = []
    counter = 0 
    
    title = ""

    while columnNumberVar > 26:
        columnNumberVar -= 26
        counter += 1

        if counter == 26:
            listVar.append(counter)
            counter = 0
    
    if len(listVar) == 0:
        listVar.append(counter)
        listVar.append(columnNumberVar)
    else:
        listVar.append(columnNumberVar)
    
    
    for i in listVar:
        title += DATABASE[i - 1]
    
    return title
        
    
DATABASE = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
columnNumber = [1,28,701]

for test in range(len(columnNumber)):
    print(colored(f"Test {(test + 1)}:", "green"),convertToTile(columnNumber[test]), "|", colored("Passed", "green"))