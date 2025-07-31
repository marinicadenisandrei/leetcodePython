# Leetcode - 190. Reverse Bits (Python language) - Easy 

from termcolor import colored
print(colored("Leetcode - 190. Reverse Bits (Python language) -","yellow"),colored("Easy","green"))

def reverseBits(nVar : str):
    numberVar = 0
    for i in range(len(nVar)):
        if nVar[i] == "1":
            numberVar += pow(2,i)
    
    return numberVar
            
n = ["00000010100101000001111010011100","11111111111111111111111111111101"]
for test in range(len(n)):
    print(colored(f"Test {(test + 1)}:","green"), reverseBits(n[test]), "|", colored("Passed","green"))