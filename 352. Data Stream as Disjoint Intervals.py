# Leetcode - 352. Data Stream as Disjoint Intervals (Python language) - Hard

from termcolor import colored

print(colored("Leetcode - 352. Data Stream as Disjoint Intervals (Python language) -","yellow"), colored("Hard","red"))

class SummaryRanges :
    def __init__(self):
        self.arr = []
    
    def addNum(self, num):
        self.arr.append(num)
    
    def getIntervals(self):
        self.arr.sort()
        intervals = []

        start = self.arr[0]

        for i in range(len(self.arr) - 1):
            if self.arr[i + 1] - self.arr[i] > 1:
                intervals.append([start, self.arr[i]])
                start = self.arr[i + 1]
                continue
                
            if (i + 1) == (len(self.arr) - 1):
                intervals.append([start, self.arr[i + 1]])
                  
        return intervals

print(colored("Test 1:","green"))

summaryRanges = SummaryRanges()

summaryRanges.addNum(1)  
print(summaryRanges.getIntervals())
summaryRanges.addNum(3)
print(summaryRanges.getIntervals())
summaryRanges.addNum(7)
print(summaryRanges.getIntervals())
summaryRanges.addNum(2)
print(summaryRanges.getIntervals())
summaryRanges.addNum(6)
print(summaryRanges.getIntervals())

print("|", colored("Passed","green"))