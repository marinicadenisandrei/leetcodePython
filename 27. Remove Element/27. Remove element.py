nums = [0,1,2,2,3,0,4,2,2]
val = 2

counter = [i for i in nums if i == val]
x = [nums.remove(val) for i in range(len(counter))]
x = [nums.append("_") for i in range(len(counter))]

print(nums)