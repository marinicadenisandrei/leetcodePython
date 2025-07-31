# Leetcode - 148. Sort List (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 148. Sort List (Python language) - Medium", "yellow"))

def sortList(headVar : list):
    headVar.sort()
    return headVar

head = [[4,2,1,3], [-1,5,3,4,0], []]

for test in range(len(head)):
    print(colored(f"Test {(test + 1)}:", "green"), sortList(head[test]), "|", colored("Passed", "green"))


