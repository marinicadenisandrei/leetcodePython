# Leetcode - 219. Contains Duplicate II (C language) - Easy

from termcolor import colored

print(colored("Leetcode - 219. Contains Duplicate II (C language) -","yellow"), colored("Easy","green"))

def containsNearbyDuplicate(numsVar: list, kVar: int):
    for i in range(len(numsVar)):
        for j in range(len(numsVar)):
            if i != j and numsVar[i] == numsVar[j] and abs(i - j) <= kVar:
                return True

    return False
                
nums = [[1,2,3,1],[1,0,1,1],[1,2,3,1,2,3]]
k = [3,1,2]

for test in range(len(k)):
    print(colored(f"Test {(test + 1)}:","green"), containsNearbyDuplicate(nums[test], k[test]), "|", colored("Passed","green"))