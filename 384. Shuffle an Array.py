# LeetCode 384. - Shuffle an Array (Python language) - Medium

from termcolor import colored

print(colored("LeetCode 384. - Shuffle an Array (Python language) - Medium", "yellow"))

class Solution:
    def __init__(self, arr):
        self.arr = arr
        self.copy = arr.copy()
    
    def reset(self):
        self.arr = self.copy.copy()
        return self.arr
    
    def shuffle(self):
        import random
        shuffled = self.arr.copy()
        n = len(shuffled)
        for i in range(n):
            j = random.randint(i, n - 1)
            shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
        return shuffled
    
solution = Solution([1, 2, 3])

print(colored(f"Test 1:", "green"),
    solution.shuffle(),
    solution.reset(),
    solution.shuffle(),
    "|",
    colored("Passed","green")
)


