# Leetcode - 445. Add Two Numbers II (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 445. Add Two Numbers II (Python language) - Medium", "yellow"))

def addTwoNumbers(l1Var, l2Var):
    n1 = int("".join(map(str, l1Var)))
    n2 = int("".join(map(str, l2Var)))

    return [int(d) for d in (str(n1 + n2))]

l1 = [[7,2,4,3],[2,4,3],[0]]
l2 = [[5,6,4],[5,6,4],[0]]

for test in range(len(l1)):
    print(
        colored(f"Test {(test + 1)}:", "green"),
        addTwoNumbers(l1[test], l2[test]),
        "|",
        colored("Passed", "green")
    )