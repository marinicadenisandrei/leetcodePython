# Leetcode - 461. Hamming Distance (Python language) - Easy

from termcolor import colored

print(colored("Leetcode - 461. Hamming Distance (Python language) -", "yellow"), colored("Easy", "green"))

def hammingDistance(xVar, yVar):
    return (xVar ^ yVar).bit_count()

x = [1,3]
y = [4,1]

for test in range(len(x)):
    print(
        colored(f"Test {(test + 1)}:", "green"),
        hammingDistance(x[test], y[test]),
        "|",
        colored("Passed", "green")
    )