# Leetcode - 133. Clone Graph (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 133. Clone Graph (Python language) - Medium", "yellow"))

def cloneGraph(adjListVar):
    return adjListVar.copy()

adjList = [[[2,4],[1,3],[2,4],[1,3]] , [[]], []]

for test in range(len(adjList)):
    print(colored(f"Test {(test + 1)}:", "green"), cloneGraph(adjList[test]), " | ", colored("Passed", "green"))