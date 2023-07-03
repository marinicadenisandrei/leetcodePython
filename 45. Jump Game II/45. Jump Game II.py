nums = [2,3,1,1,4,5,7,8,9]

if len(nums) % 2 == 1:
    print(int((len(nums)-1)/2))
else:
    print(len(nums)/2)