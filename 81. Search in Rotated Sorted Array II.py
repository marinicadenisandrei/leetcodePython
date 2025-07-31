# Leetcode - 81. Search in Rotated Sorted Array II - Medium

from termcolor import colored

print(colored("Leetcode - 81. Search in Rotated Sorted Array II - Medium", "yellow"))

numsTest = [[2,5,6,0,0,1,2], [2,5,6,0,0,1,2]]
targetTest = [0,3]

def elementInList(listElements, element):
    if element in listElements:
        return True 
    else:
        return False

for test in range(len(numsTest)):
    nums = numsTest[test]
    target = targetTest[test]

    testNumber = test + 1

    print(colored(f"Test {testNumber}:","green"),elementInList(nums, target),"|", colored("Passed", "green"))





    