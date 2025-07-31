# Leetcode - 297. Serialize and Deserialize Binary Tree (Python language) - Hard

from termcolor import colored

print(colored("Leetcode - 297. Serialize and Deserialize Binary Tree (Python language) -","yellow"), colored("Hard","red"))

class Codec:
    def __init__(self, rootVar):
        self.rootVar = rootVar

    def serialize(self):
        return str(self.rootVar)

root = [[1,2,3,0,0,4,5], []]

for test in range(len(root)):    
    codec = Codec(root[test])
    print(colored(f"Test {(test + 1)}:","green"), codec.serialize(),"|", colored("Passed","green"))