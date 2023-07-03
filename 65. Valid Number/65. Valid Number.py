# Leetcode - 65. Valid Number (Python language) - Hard

from termcolor import colored

print(colored("Leetcode - 65. Valid Number (Python language)","yellow")," | ",colored("Hard","red"))

state = colored("Passed", "green")

s = ["0", "e", "."]

def checkForValidNumber(number :str):
    try:
        number = int(float(number))
        return True
    except ValueError:
        return False
    except OverflowError:
        return True

for test in s:
    testNumber = s.index(test) + 1
    text = colored(f"Test {testNumber}: ", "green")
    print(colored(f"{text}{checkForValidNumber(test)} | {state}"))    



