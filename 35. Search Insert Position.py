nums = [1,3,5,6]
target = 7
index = None

if target in nums:
    print(nums.index(target))
else:
    for i in range(len(nums)):
        if target < nums[i]:
            index = i
            print(index)
            break

if index == None:
    print(len(nums))