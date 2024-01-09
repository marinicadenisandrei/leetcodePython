from termcolor import colored

print(colored("Leetcode - 137. Single Number II (Python language) - Medium", "yellow"))

def singleNumber(numsVar : list):
    for i in numsVar:
        if numsVar.count(i) == 1:
            return i


nums = [[2,2,3,2], [0,1,0,1,0,1,99]]
for test in range(len(nums)):
    print(colored(f"Test {(test + 1)}:", "green"), singleNumber(nums[test]), "|", colored("Passed", "green"))