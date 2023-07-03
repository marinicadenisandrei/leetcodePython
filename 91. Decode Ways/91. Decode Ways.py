# Leetcode - 91. Decode Ways (C language) - Medium

from termcolor import colored

print(colored("Leetcode - 91. Decode Ways (C language) - Medium", "yellow"))

DATABASE = {
    1 : "A",
    2 : "B",
    3 : "C",
    4 : "D",
    5 : "E",
    6 : "F",
    7 : "G",
    8 : "H",
    9 : "I",
    10 : "J",
    11 : "K",
    12 : "L",
    13 : "M",
    14 : "N",
    15 : "O",
    16 : "P",
    17 : "Q",
    18 : "R",
    19 : "S",
    20 : "T",
    21 : "U",
    22 : "V",
    23 : "W",
    24 : "X",
    25 : "Y",
    26 : 'Z'
}

sTest = ["12", "226", "06"] 

for test in range(len(sTest)):
    s = sTest[test]
    if "0" not in s:
        first = [i for i in s if i != "0"]
        s = [(s[i], s[i-1:i+1]) for i in range(1, len(s)) if s[i] != "0" and s[i-1:i+1] != "0"]
        s.append(first)
        result = len(s)
    else:
        result = 0

    testNumber = test + 1

    print(colored(f"Test {testNumber}:", "green"), result, "|", colored("Passed", "green"))



