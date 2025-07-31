# Leetcode - 330. Patching Array (Python language) - Hard

from termcolor import colored

print(colored("Leetcode - 330. Patching Array (Python language) -","yellow"), colored("Hard","red"))

def MinPatches(numsVar, nVar):
    flag = True
    counter = 0

    while flag:
        flag = False

        for i in range(len(numsVar)):
            for j in range(len(numsVar) + 1):
                if nVar in numsVar[i:j] or nVar == sum(numsVar[i:j]):
                    return counter
                else:
                    flag = True
        
        for i in range(len(numsVar)):
            if numsVar[i + 1] - numsVar[i] != 1:
                numsVar.append(numsVar[i] + 1)
                numsVar.sort()
                break    

        counter += 1            
            
nums = [1,3],[1,5,10],[1,2,2]
n = [6,20,5]

for test in range(len(n)):
    print(colored(f"Test {(test + 1)}:","green"), MinPatches(nums[test], n[test]), "|", colored("Passed","green"))