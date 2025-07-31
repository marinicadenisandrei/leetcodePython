# Leetcode - 189. Rotate Array (Python language) - Medium

from termcolor import colored
print(colored("Leetcode - 189. Rotate Array (Python language) - Medium", "yellow"))

def rotate(numsVar :list, kVar: int) -> list:
    for i in range(kVar + 1):
        numsVar.append(numsVar[0])
        numsVar.pop(0)
    
    return numsVar

nums = [[1,2,3,4,5,6,7],[-1,-100,3,99]] 
k = [3,2]

for test in range(len(nums)):
   print(colored(f"Test {(test + 1)}:","green"), rotate(nums[test],k[test]), "|", colored("Passed","green"))