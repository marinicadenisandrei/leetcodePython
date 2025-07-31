# Leetcode - 233. Number of Digit One (Python language) - Hard

from termcolor import colored

print(colored("Leetcode - 233. Number of Digit One (Python language) -","yellow"), colored("Hard","red"))

def countDigitOne(nVar: int) -> int:
    result = 0

    for i in range(nVar + 1):
        result += str(i).count("1")
    
    return result

n = [13,0]

for test in range(len(n)):
    print(colored(f"Test {(test + 1)}:","green"), countDigitOne(n[test]), "|", colored("Passed","green"))