# Leetcode - 410. Split Array Largest Sum (Python language) - Hard

from termcolor import colored

print(colored("Leetcode - 410. Split Array Largest Sum (Python language) -","yellow"), colored("Hard","red"))

def splitArray(numsVar, kVar):
    splits = []
    candidatesSums = []

    for i in range(kVar - 1):
        splits.append([numsVar[i]])
    splits.append(numsVar[kVar - 1:])

    while True:
        sums = [sum(part) for part in splits]
        maxSum = max(sums)
        candidatesSums.append(maxSum)

        noOfEle = 0
        indexMaxElements = 0
        
        for i in range(len(splits)):
            if noOfEle <= len(splits[i]):
                noOfEle = len(splits[i])
                indexMaxElements = i

        if indexMaxElements == 0:
            break

        try:
            splits[indexMaxElements - 1].append(splits[indexMaxElements][0])
            splits[indexMaxElements].pop(0)
        except IndexError:
            break

    return min(candidatesSums)


nums = [[7,2,5,10,8],[1,2,3,4,5]]
k = [2,2]

for test in range(len(nums)):
    print(
        colored(f"Test {(test + 1)}:", "green"),
        splitArray(nums[test], k[test]),
        "|",
        colored("Passed","green")
    )
