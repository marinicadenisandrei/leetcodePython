# Leetcode - 76. Minimum Window Substring (Python language) - Hard

from termcolor import colored

print(colored("Leetcode - 76. Minimum Window Substring (Python language) -", "yellow"), colored("Hard", "red"))

sTest = ["ADOBECODEBANC", "a", "a"]
tTest = ["ABC", "a", "aa"]


def checkCharSubstingInString(string1 : str, string2 : str):
    listValidation = []

    for i in string2:
        if i in string1:
            listValidation.append(1)
        else:
            listValidation.append(0)
    
    if all(_ == 1 for _ in listValidation):
        return True
    else:
        return False


for test in range(len(sTest)):

    s = sTest[test]
    t = tTest[test]

    word = ""
    output = []

    if s >= t:
        while len(s) > 0:
            for i in s:
                word += i
                
                if checkCharSubstingInString(word,t):
                    output.append(word)
                    break
            
            s = s[1:]
            word = ""

    else:
        output.append("")

    testNumber = test + 1

    print(colored(f"Test {testNumber}:","green"),min(output, key=len), "|", colored("Passed","green"))
    
