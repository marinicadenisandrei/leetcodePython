# Leetcode - 70. Climbing Stairs (Python language) - Easy 

from itertools import permutations
from termcolor import colored

print(colored("Leetcode - 70. Climbing Stairs (Python language) - ", "yellow"), colored("Easy", "green"))

state = colored("Passed", "green")

nTest = [2,3]

for test in nTest:
    n = test
    output = []

    ways = 1

    for i in range(n):
        output.append(1)

    while output[0] == 1 and output [1] == 1:
        output = output[2:]
        output.append(2)

        permutationsList = list(permutations(output))
        permutationsList = list(dict.fromkeys(permutationsList))
        
        ways += len(permutationsList)

        permutationsList = []

    testNumber = nTest.index(test) + 1
    text = colored(f"Test {testNumber}: ", "green")

    print(f"{text}{ways} | {state}")
