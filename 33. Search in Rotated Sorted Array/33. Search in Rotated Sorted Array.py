nums = [4,5,6,7,0,1,2]

target = 0

index = []
for i in range(len(nums)):
    if nums[i] == target:
        index.append(i)

if len(index) == 1:
    print(index[0])
elif len(index) == 0:
    print("-1")