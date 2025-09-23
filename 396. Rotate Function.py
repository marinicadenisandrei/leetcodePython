# Leetcode - 396. Rotate Function (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 396. Rotate Function (Python language) - Medium","yellow"))

def maxRotateFunction(numsVar):
    result = 0

    numsVarCopy = numsVar.copy()
    
    first = numsVar[0]
    numsVar.pop(0)
    numsVar.append(first)

    while numsVar != numsVarCopy:
        temp = 0

        for i in range(len(numsVar)):
            temp += i * numsVar[i]
        
        if result < temp:
            result = temp
        
        first = numsVar[0]
        numsVar.pop(0)
        numsVar.append(first)
            
    return result
        
nums = [[4,3,2,6],[100]]

for test in range(len(nums)):
    print(
        colored(f"Test {(test + 1)}:","green"),
        maxRotateFunction(nums[test]),
        "|",
        colored("Passed","green")
    )
    