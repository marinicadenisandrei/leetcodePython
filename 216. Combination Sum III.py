# Leetcode - 216. Combination Sum III (Python language) - Medium

from termcolor import colored
print(colored("Leetcode - 216. Combination Sum III (Python language) - Medium","yellow"))

def combinationSum3(kVar: int, nVar: int):
    acumulation = [i for i in range(1, nVar + 1)]
    candidates = []
    result = []
    
    while len(acumulation) > kVar:
        temp = [acumulation[i] for i in range(kVar)]
        candidates.append(temp)        
        acumulation.pop(0)

    for i in candidates:
        copy = i.copy()

        for j in range(len(i)):
            for k in range(1, nVar + 1):
                copy[j] = k

                sortCopy = copy.copy()
                sortCopy.sort()

                has_duplicates = len(sortCopy) != len(set(sortCopy))

                if sum(sortCopy) == nVar and sortCopy not in result and not has_duplicates:
                    result.append(sortCopy.copy())
                    
            copy = i.copy()
                
    return result
    
k = [3,3,4]
n = [7,9,1]

for test in range(len(k)):
    print(colored(f"Test {(test + 1)}:","green"),combinationSum3(k[test],n[test]),"|", colored("Passed","green"))