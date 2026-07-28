# Leetcode - 446. Arithmetic Slices II - Subsequence (Python language) - Hard

from termcolor import colored

print(colored("Leetcode - 446. Arithmetic Slices II - Subsequence (Python language) -", "yellow"), colored("Hard", "red"))

def numberOfArithmeticSlices(numsVar):
    allTheSameFlag = len(list(set(numsVar))) == 1

    if allTheSameFlag == 1:
        return (len(numsVar) - 1) ** 2
    
    result = 0

    for i in range(len(numsVar)):
        step = i
        acc = []
        index1 = 0
        index2 = 1
    
        while index2 < len(numsVar):
            if numsVar[index2] - numsVar[index1] == step:
                if len(acc) == 0:
                    acc.append(numsVar[index1])
                    acc.append(numsVar[index2])
                else:
                    acc.append(numsVar[index2])
    
                index1 = index2
            index2 += 1  

            if len(acc) > 2:
                result += len(acc) - 2

    return result

nums = [[2,4,6,8,10],[7,7,7,7,7]]

for test in range(len(nums)):
    print(
        colored(f"Test {(test + 1)}:", "green"),
        numberOfArithmeticSlices(nums[test]),
        "|",
        colored("Passed", "green")
    )

