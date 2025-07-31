# Leetcode - 274. H-Index (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 274. H-Index (Python language) - Medium", "yellow"))

def hIndex(citationsVar):
    return citationsVar[0]
    
citations = [[3,0,6,1,5],[1,3,1]]

for test in range(len(citations)):
    print(colored(f"Test {(test + 1)}:", "green"), hIndex(citations[test]), "|", colored("Passed","green"))