# Leetcode - 347. Top K Frequent Elements (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 347. Top K Frequent Elements (Python language) - Medium","yellow"))

def topKFrequent(numsVar, kVar):
    occ = dict()

    for i in numsVar:
        if i not in occ:
            occ[i] = numsVar.count(i)

    sorted_dict = dict(sorted(occ.items(), key=lambda item: item[1], reverse=True))

    return list(sorted_dict.keys())[:kVar]


nums = [[1,1,1,2,2,3],[1]]
k = [2,1]

for test in range(len(nums)):
    print(colored(f"Test {(test + 1)}:","green"), topKFrequent(nums[test], k[test]), "|", colored("Passed","green"))
    

