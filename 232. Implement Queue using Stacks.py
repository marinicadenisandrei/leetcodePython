from termcolor import colored

print(colored("Leetocode - 232. Implement Queue using Stacks (Python language) -","yellow"), colored("Easy","green"))

class MyQueue:
    def __init__(self):
        self.queue = []
        self.cache = [0]

    def push(self, element):
        self.queue.append(element)
        self.cache.append(0)

    def pop(self):
        temp = self.queue[0]
        self.queue.pop(0)
        self.cache.append(temp)
        return temp
    
    def peek(self):
        self.cache.append(self.queue[0])
        return self.queue[0]
    
    def empty(self):
        flag = len(self.queue) == 0
        self.cache.append(flag)
        return flag

    def returnCache(self):
        return self.cache
        
        
myQueue = MyQueue()
myQueue.push(1)
myQueue.push(2)
myQueue.peek()
myQueue.pop()
myQueue.empty()
print(colored("Test 1:","green"), myQueue.returnCache(), "|", colored("Passed","green"))


