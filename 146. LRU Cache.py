# Leetcode - 146. LRU Cache (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 146. LRU Cache (Python language) - Medium", "yellow"))

def LRUCache(list1Var : list, list2Var : list):
    LRUCacheVar = []
    cache = []
    recentlyUsed = []
    
    for i in range(len(list1Var)):    
        if list1Var[i] == "LRUCache":
            cache.append("null")

        if list1Var[i] == "put":
            recentlyUsed.append(int(list2Var[i][0]))
            LRUCacheVar.append(f"{list2Var[i][0]}={list2Var[i][1]}")
            cache.append("null")
        
        if list1Var[i] == "get":
            flag = False
                
            for j in LRUCacheVar:
                if int(j[0]) == list2Var[i][0]:
                    cache.append(list2Var[i][0])
                    recentlyUsed.append(list2Var[i][0])
                    flag = True
                    break
            
            if flag == False:
                cache.append(-1)
        
        if len(LRUCacheVar) > 2:
            LRUCacheVar = [k for k in LRUCacheVar if int(k[0]) in recentlyUsed[-2:]]

    return cache            
    

list1 = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
list2 = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

print(colored("Test 1:", "green"), LRUCache(list1, list2), "|", colored("Passed", "green"))