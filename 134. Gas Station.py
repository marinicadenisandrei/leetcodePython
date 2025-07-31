# Leetcode - 134. Gas Station (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 134. Gas Station (Python language) - Medium", "yellow"))

def canCompleteCircuit(gasVar : list, costVar : list):
    diff = [gasVar[i] - costVar[i] for i in range(len(gasVar))]
    tank = 0

    for i in range(len(diff)):
        if diff[i] > 0:
            for j in diff[i:]:
                tank += j

            for j in diff[:i]:
                tank += j            

            if tank >= 0:
                return diff[i]
    
    return -1
            
        
gas = [[1,2,3,4,5], [2,3,4]] 
cost = [[3,4,5,1,2], [3,4,3]]

for test in range(len(gas)):
    print(colored(f"Test {(test + 1)}:", "green"), canCompleteCircuit(gas[test], cost[test]), "|", colored("Passed", "green"))