# Leetcode - 405. Convert a Number to Hexadecimal (Python language) - Easy

from termcolor import colored

print(colored("Leetcode - 405. Convert a Number to Hexadecimal (Python language) -", "yellow"), colored("Easy", "green"))

def toHex(numVar):
    return str(hex(numVar & 0xFFFFFFFF)).replace("-","").replace("0x","")

num = [26,-1]

for test in range(len(num)):    
    print(
        colored(f"Test {(test + 1)}:","green"),
        toHex(num[test]),
        "|",
        colored("Passed","green")
    )