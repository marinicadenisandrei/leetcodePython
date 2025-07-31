# Leetcode - 374. Guess Number Higher or Lower (Python language) - Easy

from termcolor import colored

print(colored("Leetcode - 374. Guess Number Higher or Lower (Python language) -", "yellow"), colored("Easy","green"))

def guessNumber(nVar, pickVar):
    low = 1
    high = nVar

    while low <= high:
        mid = low + (high - low) // 2

        if mid == pickVar:
            return mid
        elif mid > pickVar:
            high = mid - 1
        else:
            low = mid + 1
    
    return -1
            
n = [10,1,2]
pick = [6,1,1]

for test in range(len(n)):
    print(colored(f"Test {(test + 1)}:","green"), guessNumber(n[test], pick[test]), "|", colored("Passed","green"))
    
    

