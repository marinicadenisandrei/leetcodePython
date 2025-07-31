# Leeetcode - 195. Tenth Line (Python language) - Easy

from termcolor import colored

print(colored("Leeetcode - 195. Tenth Line (Python language) -","yellow"), colored("Easy", "green"))

def tenthLine(fileVar: str):
    return fileVar.split("\n")[9]

file = "Line 1\nLine 2\nLine 3\nLine 4\nLine 5\nLine 6\nLine 7\nLine 8\nLine 9\nLine 10"
print(colored("Test 1:","green"), tenthLine(file), "|", colored("Passed","green"))

