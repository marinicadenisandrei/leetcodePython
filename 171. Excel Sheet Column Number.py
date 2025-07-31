# Leetcode - 171. Excel Sheet Column Number (Python language) - Easy

from termcolor import colored

print(colored("Leetcode - 171. Excel Sheet Column Number (Python language) -", "yellow"), colored("Easy","green"))

ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def titleToNumber(columnTitleVar: str):
    result = ALPHABET.index(columnTitleVar[-1]) + 1
    
    for i in reversed(range(len(columnTitleVar) - 1)):
        result += (ALPHABET.index(columnTitleVar[i]) + 1) * 26
    
    return result

columnTitle = ["A","AB","ZY"]

for test in range(len(columnTitle)):
    print(colored(f"Test {(test + 1)}:","green"),titleToNumber(columnTitle[test]),"|",colored("Passed","green"))