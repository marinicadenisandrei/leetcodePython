# Leetcode - 14. Longest Common Prefix (Python language) - Easy

from termcolor import colored

print(colored("Leetcode - 14. Longest Common Prefix (Python language) -","yellow"), colored("Easy","green"))

strsTest = [["flower","flow","flight"], ["dog","racecar","car"]]

for test in range(len(strsTest)):
    strs = strsTest[test]
    firstChars = ""
    output = ""

    for i in range(len(strs)):
        flag = False
        for j in range(len(min(strs, key= len)) - 1):
            firstChars += strs[j][i]

        if firstChars.count(firstChars[0]) == len(strs):
            output += firstChars[0]
        else:
            break

        firstChars = ""

    testNumber = test + 1
    print(colored(f"Test {testNumber}:","green"),output,"|", colored("Passed","green"))
    






