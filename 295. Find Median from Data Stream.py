# Leetcode - 295. Find Median from Data Stream (Python language) - Hard

from termcolor import colored

print(colored("Leetcode - 295. Find Median from Data Stream (Python language) -","yellow"), colored("Hard","red"))

class MedianFinder:
    def __init__(self):
        self.medianList = []

    def addNum(self, numVar):
        self.medianList.append(numVar)
        
    def findMedian(self):
        return sum(self.medianList) / len(self.medianList)
    

print(colored("Test 1:","green"))
medianFinder = MedianFinder();
medianFinder.addNum(1)
medianFinder.addNum(2)
print(medianFinder.findMedian())
medianFinder.addNum(3)
print(medianFinder.findMedian())
print("|", colored("Passed","green"))

