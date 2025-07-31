# Leetcode - 342. Power of Four (Python language) - Easy

from termcolor import colored

print(colored("Leetcode - 342. Power of Four (Python language) -",'yellow'), colored("Easy","green"))

def is_power_of_four(nVar):
    return nVar > 0 and (nVar & (nVar - 1)) == 0 and (nVar - 1) % 3 == 0

n = [16,5,1]

for test in range(len(n)):
    print(colored(f"Test {(test + 1)}:","green"), is_power_of_four(n[test]), "|", colored("Passed","green"))
    


