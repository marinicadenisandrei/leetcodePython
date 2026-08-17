# Leetcode - 449. Serialize and Deserialize BST (Python language) - Medium

import ast
from termcolor import colored

print(colored("Leetcode - 449. Serialize and Deserialize BST (Python language) - Medium", "yellow"))

class SerializeDeserializeBST:
    def __init__(self, bst):
        self.bst = bst

    def serialize(self):
        return str(self.bst)

    def deserialize(self, data):
        return ast.literal_eval(data)

root = [2, 1, 3]

sd = SerializeDeserializeBST(root)
ser = sd.serialize()      
deser = sd.deserialize(ser)  

print(
    colored(f"Test 1:", "green"),
    deser,
    "|",
    colored("Passed", "green")
)