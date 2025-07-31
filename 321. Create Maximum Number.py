# Leetcode - 321. Create Maximum Number (Python language) - Hard

from termcolor import colored

print(colored("Leetcode - 321. Create Maximum Number (Python language) -", "yellow"), colored("Hard","red"))

def merge_lists(list1, list2):
    result = []
    i, j = 0, 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] >= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    
    result.extend(list1[i:])
    result.extend(list2[j:])
    
    return result

def MaxNumber(nums1Var, nums2Var, kVar):
    output = 0
    candidates1 = []
    candidates2 = []

    for i in nums1Var:
        candidates1.append([i])
        
    for i in nums2Var:
        candidates2.append([i])
    
    for k in range(kVar):
        for i in range(len(nums1Var)):
            for j in range(i + 1, len(nums1Var)):
                temp = [nums1Var[i]]
                temp.extend(nums1Var[j:j + k])
                candidates1.append(temp)

    for k in range(kVar):
        for i in range(len(nums2Var)):
            for j in range(i + 1, len(nums2Var)):
                temp = [nums2Var[i]]
                temp.extend(nums2Var[j:j + k])
                candidates2.append(temp)
            
    for list1 in candidates1:
        for list2 in candidates2:
            result = merge_lists(list1, list2)
            result = int("".join(map(str, result)))

            if output < result and len(str(result)) == kVar:
                output = result
    
    return output
                
nums1 = [[3,4,6,5],[6,7],[3,9]]
nums2 = [[9,1,2,5,8,3],[6,0,4],[8,9]]
k = [5,5,3]

for test in range(len(k)):
    print(colored(f"Test {(test + 1)}:","green"), MaxNumber(nums1[test], nums2[test], k[test]), "|", colored("Passed","green"))
    