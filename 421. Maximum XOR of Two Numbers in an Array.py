# Leetcode - 421. Maximum XOR of Two Numbers in an Array (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 421. Maximum XOR of Two Numbers in an Array (Python language) - Medium","yellow"))

def findMaximumXOR(numsVar):
    result = 0

    for i in range(len(numsVar)):
        for j in range(len(numsVar)):
            temp = numsVar[i] ^ numsVar[j]

            if temp > result:
                result = temp
    
    return result

nums = [[3,10,5,25,2,8],[14,70,53,83,49,91,36,80,92,51,66,70]]

for test in range(len(nums)):
    print(
        colored(f"Test {(test + 1)}:", "green"),
        findMaximumXOR(nums[test]),
        "|",
        colored("Passed", "green")
    )