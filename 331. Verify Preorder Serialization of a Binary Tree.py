# Leetcode - 331. Verify Preorder Serialization of a Binary Tree (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 331. Verify Preorder Serialization of a Binary Tree (Python language) - Medium","yellow"))

def IsValidSerialization(preorderVar):
    root = preorderVar.split(",")
    mid = int(len(root) / 2)

    left = [i for i in root[:mid] if i != "#"]
    right = [i for i in root[mid:] if i != "#"]

    if (len(left) == 0 or len(right) == 0) or (len(left) + len(right)) < 3:
        return False

    if len(left) % len(right) == 0:
        return True

    return False
        
preorder = ["9,3,4,#,#,1,#,#,2,#,6,#,#","1,#","9,#,#,1"]

for test in range(len(preorder)):
    print(colored(f"Test {(test + 1)}:","green"), IsValidSerialization(preorder[test]), "|", colored("Passed","green"))
    
    