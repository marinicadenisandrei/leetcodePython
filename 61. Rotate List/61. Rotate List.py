# Leetcode - 61. Rotate List

from termcolor import colored

problem = colored("Leetcode - 61. Rotate List", "yellow")
print(f"{problem}")

head = [[1,2,3,4,5],[0,1,2]] 
k = [2,4]
state = colored("Passed", "green")

for test in range(len(head)):
    output = head[test][len(head[test])-k[test]:].copy()
    output.extend(head[test][:len(head[test])-k[test]].copy())

    noTest = test+1
    text = colored(f"Test {noTest}: ", "green")
    print(f"{text}{output} | {state}")
    output = []
