# Leetcode - 160. Intersection of Two Linked Lists (Python language) - Easy

from termcolor import colored

print(colored(f"Leetcode - 160. Intersection of Two Linked Lists (Python language) -", "yellow"),colored("Easy","green"))

def getIntersectionNode(intersectValVar:int, listAvar:list, listBvar:list, skipAvar:int, skipBvar:int):
    if intersectValVar in listAvar and intersectValVar in listBvar:
        index1 = listAvar.index(intersectValVar)
        index2 = listBvar.index(intersectValVar)

        listAvar = listAvar[index1:]
        listBvar = listBvar[index2:]

        if listAvar == listBvar:
            return f"Intersected at {intersectValVar}"
    
    return "No intersection"
           
intersectVal = [8,2,0] 
listA = [[4,1,8,4,5],[1,9,1,2,4],[2,6,4]]
listB = [[5,6,1,8,4,5],[3,2,4],[1,5]]
skipA = [2,3,3]
skipB = [3,1,2]

for test in range(len(intersectVal)):
    print(colored(f"Test {(test + 1)}:","green"),getIntersectionNode(intersectVal[test], listA[test], listB[test], skipA[test], skipB[test]),"|",colored("Passed","green"))