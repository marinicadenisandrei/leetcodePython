list1 = [1,2]
list2 = [4,3,5,6,7,8,9,0,4567,2]
list1.extend(list2)
list1.sort()
print(list1)

if len(list1)% 2 == 0:
    mid_impar_1 = [list1[int(len(list1)/2)-1],list1[int(len(list1)/2)]]
    mid_impar_1 =  (mid_impar_1[0] + mid_impar_1[1])/2
    print(mid_impar_1)
    
else:
    print(list1[int(len(list1)/2)])




