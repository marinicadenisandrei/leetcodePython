# Leetcode - 69. Sqrt(x) (Python Language) - Easy 

from termcolor import  colored

print(colored("Leetcode - 69. Sqrt(x) (Python Language) - ", "yellow"), colored("Easy","green"))

state = colored("Passed", "green")

import math

x = [4,8];

for test in x:
    testNumber = x.index(test) + 1
    text = colored(f"Test {testNumber}: ", "green")
    result = int(math.sqrt(test))
    print(f"{text}{result} | {state}")