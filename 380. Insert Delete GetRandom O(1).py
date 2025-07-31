# Leetcode - 380. Insert Delete GetRandom O(1) (Python language) - Medium

import random
from termcolor import colored

print(colored("Leetcode - 380. Insert Delete GetRandom O(1) (Python language) - Medium","yellow"))

class RandomizedSet:
    def __init__(self):
        self.setList = []

    def insert(self, val: int) -> bool:
        if val not in self.setList:
            self.setList.append(val)
            return True

        return False
    
    def remove(self, val: int) -> bool:
        if val in self.setList:
            self.setList.remove(val)
            return True

        return False

    def getRandom(self) -> int:
        return self.setList[random.randint(0,len(self.setList) - 1)]
    
randomizeSet = RandomizedSet()
print(
    colored("Test 1:","green"),
    randomizeSet.insert(1), 
    randomizeSet.remove(2), 
    randomizeSet.insert(2),
    randomizeSet.getRandom(),
    randomizeSet.remove(1),
    randomizeSet.insert(2),
    randomizeSet.getRandom(),
    "|",
    colored("Passed","green"))





