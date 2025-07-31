# Leetcode - 191. Number of 1 Bits (Python language) - Easy

from termcolor import colored

print(colored("Leetcode - 191. Number of 1 Bits (Python language) -", "yellow"), colored("Easy","green"))

def hammingWeight(nVar: int) -> int:
    binary = ""

    while nVar > 0:
        if nVar % 2 == 1:  
            binary = "1" + binary  
        else:
            binary = "0" + binary 
        
        nVar = nVar // 2

    return binary.count("1")

n = [11,128,2147483645]

for test in range(len(n)):
    print(colored(f"Test {(test + 1)}:", "green"), hammingWeight(n[test]), "|", colored("Passed", "green"))
