# Leetcode - 381. Insert Delete GetRandom O(1) - Duplicates allowed (Python language) - Hard

import random
from termcolor import colored

print(colored("Leetcode - 381. Insert Delete GetRandom O(1) - Duplicates allowed -","yellow"), colored("Hard","red"))

class RandomizedCollection:
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
    
randomizedCollection = RandomizedCollection()

print(
    colored("Test 1:","green"),
    randomizedCollection.insert(1),
    randomizedCollection.insert(1),
    randomizedCollection.insert(2),
    randomizedCollection.getRandom(),
    randomizedCollection.remove(1),
    randomizedCollection.getRandom(),
    "|",
    colored("Passed","green"))
 