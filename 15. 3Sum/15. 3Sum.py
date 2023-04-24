nums = [-1,0,1,2,-1,-4]
final = []

for i in range(len(nums)):
    for j in range(len(nums)):
        for k in range(len(nums)):
            if nums[i] + nums[j] + nums[k] == 0 and i != j and j != k and j != k and i != k:
                print(i,j,k)
                final.append([nums[i],nums[j],nums[k]])

final = [sorted(i) for i in final]

new_list = []

[new_list.append(item) for item in final if item not in new_list]

print(new_list)