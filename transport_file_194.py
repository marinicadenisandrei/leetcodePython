# Leetcode - 194. Transpose File (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 194. Transpose File (Python language) - Medium", "yellow"))

def transportFile(fileVar: str) -> str:
    fileVar = fileVar.split("\n")
    fileVar = list(filter(lambda x: x != "", fileVar))
    fileVar = [i.split(" ") for i in fileVar]
    
    string = ""
    
    for i in range(len(fileVar[0])):
        for j in range(len(fileVar)):
            string += fileVar[j][i] + " "
    
        if i < len(fileVar[0]) - 1:
            string += "\n"
    
    return string
        
file = "name age\nalice 21\nryan 30\n"

print(colored("Test 1:","green"))
print(transportFile(file))
print("|",colored("Passed","green"))