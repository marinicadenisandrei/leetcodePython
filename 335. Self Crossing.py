# Leetcode - 335. Self Crossing (Pyhon language) - Hard

from termcolor import colored

print(colored("Leetcode - 335. Self Crossing (Pyhon language) -","yellow"), colored("Hard","red"))

def isSelfCrossing(distanceVar):
    return len(distanceVar) != len(list(dict.fromkeys(distanceVar)))
    
distance = [[2,1,1,2],[1,2,3,4],[1,1,1,2,1]]

for test in range(len(distance)):
    print(colored(f"Test {(test + 1)}:","green"), isSelfCrossing(distance[test]), "|", colored("Passed","green"))
    