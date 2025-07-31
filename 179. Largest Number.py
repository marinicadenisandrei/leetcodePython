# Leetcode - 179. Largest Number (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 179. Largest Number (Python language) - Medium","yellow"))

def largestNumber(numsVar: list):
    numsVar = [str(i) for i in numsVar]
    numsVar = sorted(numsVar, key=lambda x:x[0])[::-1]
    result = ""

    for i in range(len(numsVar) - 1,0,-2):
        stringVar1 = str(numsVar[i]) + str(numsVar[i - 1])
        stringVar2 = str(numsVar[i - 1]) + str(numsVar[i])
        
        if int(stringVar1) > int(stringVar2):
            result = stringVar1 + result
        else:
            result = stringVar2 + result
            
    if len(numsVar) % 2 == 1:
        result = numsVar[0] + result

    return result

nums = [[10,2],[3,30,34,5,9]]
for test in range(len(nums)):
    print(colored(f"Test {(test + 1)}:","green"), largestNumber(nums[test]), "|", colored("Passed", "green"))