# Leetcode - 440. K-th Smallest in Lexicographical Order (Python language) - Hard 

from termcolor import colored

print(colored("Leetcode - 440. K-th Smallest in Lexicographical Order (Python language) -", "yellow"), colored("Hard", "red"))

def findKthNumber(nVar, kVar):
    acc = []
    for i in range(1,nVar + 1):
        acc.append(str(i))

    acc = sorted(acc, key=lambda x: x[0])

    return acc[kVar - 1]

n = [13,1]
k = [2,1]

for test in range(len(n)):
    print(
        colored(f"Test {(test + 1)}:", "green"),
        findKthNumber(n[test], k[test]),
        "|",
        colored("Passed", "green")
    )