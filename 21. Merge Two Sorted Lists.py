list1 = [1,2,4]
list2 = [1,3,4]

list1.extend(list2)

final = []

for i in range(len(list1)):
    
    try:
        if list1[i] > list1[i+1]:
            list1[i], list1[i+1] = list1[i+1], list1[i]
            
            for j in range(i-1,0,-1):
                if list1[i] < list1[j]:
                    list1[i], list1[j] = list1[j], list1[i]
    except IndexError:
        pass

        
print(list1)

