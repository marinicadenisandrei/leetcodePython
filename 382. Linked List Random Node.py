# Leetcode - 382. Linked List Random Node (Python language) - Medium

import random
from termcolor import colored

print(colored("Leetcode - 382. Linked List Random Node (Python language) - Medium","yellow"))

class Solution:
    def __init__(self, items=[]):
        self.setList = items.copy()

    def getRandom(self) -> int:
        return self.setList[random.randint(0,len(self.setList) - 1)]
    
solution = [Solution([1, 2, 3])]

for test in range(len(solution)):
    print(
        colored(f"Test {(test + 1)}:","green"),
        solution[test].getRandom(), 
        solution[test].getRandom(), 
        solution[test].getRandom(), 
        solution[test].getRandom(), 
        solution[test].getRandom(),
        "|",
        colored("Passed","green"))