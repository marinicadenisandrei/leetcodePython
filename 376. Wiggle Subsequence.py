# Leetcode - 376. Wiggle Subsequence (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 376. Wiggle Subsequence (Python language) - Medium","yellow"))

def wiggleMaxLength(numsVar):
    positive = True
    index = 0
    reminder = numsVar[1]
    counter = 0

    while index < len(numsVar):
        if positive:
            if reminder - numsVar[index] > 0:
                positive = False
                reminder = numsVar[index]
                counter += 1
        else:
            if reminder - numsVar[index] < 0:
                positive = True
                reminder = numsVar[index]
                counter += 1
        
        index += 1
    
    return counter

nums = [[1,7,4,9,2,5],[1,17,5,10,13,15,10,5,16,8],[1,2,3,4,5,6,7,8,9]]

for test in range(len(nums)):
    print(colored(f"Test {(test + 1)}:","green"), wiggleMaxLength(nums[test]), "|", colored("Passed","green"))
    


