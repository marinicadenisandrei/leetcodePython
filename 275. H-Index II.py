# Leetcode - 275. H-Index II (Python language) - Medium 

from termcolor import colored
print(colored("Leetcode - 275. H-Index II (Python language) - Medium",'yellow'))

def hIndex(citationsVar):
    candidate = citationsVar[0]

    for i in range(1, len(citationsVar)):
        if i == citationsVar[i - 1]:
            candidate = citationsVar[i - 1]
    
    return candidate
            
citations = [[0,1,3,5,6],[1,2,100]]

for test in range(len(citations)):
    print(colored(f"Test {(test + 1)}:","green"), hIndex(citations[test]), "|", colored("Passed","green"))