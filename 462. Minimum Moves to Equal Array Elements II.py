# Leetcode - 462. Minimum Moves to Equal Array Elements II (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 462. Minimum Moves to Equal Array Elements II (Python language) - Medium", "yellow"))

def minMoves2(numsVar):
    result = 0
    numsVarLen = len(numsVar)

    numsVar = sorted(numsVar)
    mid = int(numsVarLen / 2)

    if numsVarLen % 2 == 0:
        numsVar.insert(mid, numsVar[mid])
        numsVarLen += 1

    pivot = numsVar[mid]

    for i in range(int(numsVarLen / 2)):
        result += (pivot - numsVar[i]) + (numsVar[numsVarLen - 1 - i] - pivot)

    return result

nums = [[1,2,3],[1,10,2,9]]

for test in range(len(nums)):
    print(
        colored(f"Test {(test + 1)}:", "green"),
        minMoves2(nums[test]), 
        "|",
        colored("Passed","green")
    )