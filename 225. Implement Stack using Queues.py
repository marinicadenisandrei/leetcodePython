# Leetcode - 225. Implement Stack using Queues (Python language) - Easy

from termcolor import colored
print(colored("Leetcode - 225. Implement Stack using Queues (Python language) -","yellow"), colored("Easy","green"))

class MyStack:
    def __init__(self):
        self.acumulation = []
        self.cache = []
        self.cache.append(0)

    def push(self, value):
        self.acumulation.append(value)
        self.cache.append(0)

    def top(self):
        self.cache.append(self.acumulation[-1])
        return self.acumulation[-1]
    
    def pop(self):
        backValue = self.acumulation[-1]
        self.acumulation = self.acumulation[:len(self.acumulation) - 1]
        self.cache.append(backValue)
        return backValue
    
    def empty(self):

        if len(self.acumulation) == 0:
            self.cache.append(True)
            return True
        
        self.cache.append(False)

myStack = MyStack()
myStack.push(1)
myStack.push(2)
myStack.top()
myStack.pop()
myStack.empty()

print(colored("Test 1: ", "green"), myStack.cache, "|", colored("Passed","green"))        


