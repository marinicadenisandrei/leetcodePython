# Leetcode - 338. Counting Bits (Python language) - Easy

from termcolor import colored

print(colored("Leetcode - 338. Counting Bits (Python language) -","yellow"), colored("Easy","green"))

def countBits(nVar):
    result = []

    for i in range(0, nVar + 1):
        result.append(str(bin(i)[2:]).count("1"))
    
    return result

n = [2,5]

for test in range(len(n)):
    print(colored(f"Test {(test + 1)}:","green"), countBits(n[test]), "|", colored("Passed","green"))