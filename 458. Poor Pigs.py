# Leetcode - 458. Poor Pigs (Python language) - Hard

from termcolor import colored

print(colored("Leetcode - 458. Poor Pigs (Python language) -", "yellow"), colored("Hard", "red"))

def poorPigs(bucketsVar, minutesToDieVar, minutesToTestVar):
    state = minutesToTestVar / minutesToDieVar + 1
    pigs = 0
    possibilities = 1

    while possibilities < bucketsVar:
        possibilities *= state
        pigs += 1

    return pigs

buckets = [4,4]
minutesToDie = [15,15]
minutesToTest = [15,30]

for test in range(len(buckets)):
    print(
        colored(f"Test {(test + 1)}:", "green"),
        poorPigs(buckets[test], minutesToDie[test], minutesToTest[test]),
        "|",
        colored("Passed", "green")
    )