# Leetcode - 371. Sum of Two Integers (Python language) - Easy

from termcolor import colored

print(colored("Leetcode - 371. Sum of Two Integers (Python language) -","yellow"), colored("Easy","green"))

def getSum(aVar, bVar):
    return aVar + bVar

a = [1,2]
b = [2,3]

for test in range(len(a)):
    print(colored(f"Test {(test + 1)}:","green"), getSum(a[test], b[test]), "|", colored("Passed","green"))