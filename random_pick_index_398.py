# Leetcode - 398. Random Pick Index (Python language) - Medium

import random
from termcolor import colored

print(colored("Leetcode - 398. Random Pick Index (Python language) - Medium","yellow"))

class Solution:
    def __init__(self, list):
        self.list = list

    def pick(self, x):
        candidates = [i for i in range(len(self.list)) if self.list[i] == x]
        return candidates[random.randint(0, len(candidates)) - 1]

solution = Solution([1,2,3,3,3])
print(
    colored("Test 1:","green"),
    solution.pick(3),
    solution.pick(1),
    solution.pick(3),
    "|",
    colored("Passed","green")
)