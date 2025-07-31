nums = [-1,0,1,2,-1,-4]
final = []

for i in nums:
    for j in nums:
        for k in nums:
            if i+j+k == 0:
                final.append([i,j,k])

final = [sorted(i) for i in final]

new_list = []

[new_list.append(item) for item in final if item not in new_list]

print(new_list)