# Leetcode - 299. Bulls and Cows (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 299. Bulls and Cows (Python language) - Medium","yellow"))

def getHint(secretVar, guessVar):
    bulls = 0
    cows = 0

    for i in range(len(secretVar) - 1):
        if secretVar[i] == guessVar[i]:
            bulls += 1
            secretVar = secretVar[:i] + secretVar[i + 1:]
            guessVar = guessVar[:i] + guessVar[i + 1:]
            i -= 1
    
    for i in secretVar:
        if i in guessVar:
            cows += 1
    
    return f"{bulls}A{cows}B"
        

secret = ["1807","1123"]
guess = ["7810","0111"]

for test in range(len(secret)):
    print(colored(f"Test {(test + 1)}:","green"), getHint(secret[test], guess[test]), "|", colored("Passed","green"))