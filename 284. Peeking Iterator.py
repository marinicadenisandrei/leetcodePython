# Leetcode - 284. Peeking Iterator (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 284. Peeking Iterator (Python language) - Medium","yellow"))

class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator.copy()
        self.iteratorIndex = 0

    def peek(self):
        try:
            return self.iterator[self.iteratorIndex]
        except IndexError:
            return -1
        
    def next(self):
        self.iteratorIndex += 1

        try:
            return self.iterator[self.iteratorIndex - 1]
        except IndexError:
            return -1
        

    def hasNext(self):
        if self.iteratorIndex > len(self.iterator) - 1:
            return False

        return True
            

peekingIterator = PeekingIterator([1,2,3])
print(colored("Test 1:", "green"), peekingIterator.next(), peekingIterator.peek(), peekingIterator.next(), peekingIterator.next(), peekingIterator.hasNext(), "|", colored("Passed","green"))
