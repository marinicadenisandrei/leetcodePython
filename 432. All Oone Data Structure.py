# Leetcode - 432. All O`one Data Structure (Python language) - Hard

from termcolor import colored

print(colored("Leetcode - 432. All O`one Data Structure (Python language) -", "yellow"), colored("Hard","red"))

class AllOne:
    # Constructor (initializer)
    def __init__(self):
        self.wordsCount = {}

    def inc(self, word):
        if word not in self.wordsCount:
            self.wordsCount[word] = 0
        else:
            self.wordsCount[word] += 1
    
    def getMaxKey(self):
        return max(self.wordsCount, key=self.wordsCount.get)

    def getMinKey(self):
        return min(self.wordsCount, key=self.wordsCount.get)

allOne = AllOne()

print(colored(f"Test 1:","green"))

print(
    allOne.inc("hello"),
    allOne.inc("hello"),
    allOne.getMaxKey(),
    allOne.getMinKey(),
    allOne.inc("leet"),
    allOne.getMaxKey(),
    allOne.getMinKey()
)

print("|", colored("Passed","green"))