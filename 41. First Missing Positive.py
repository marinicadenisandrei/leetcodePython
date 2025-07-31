nums = [7,8,9,11,12]
# nums = [1,2,0]
# nums = [3,4,-1,1]

nums.sort()
print(nums)

for i in nums:
    if i < 0:
        nums.remove(i)

flag_intre = 0
flag_start = 0

if nums[0] > 1:
    print(1)
    flag_start = 1

if flag_start == 0:
    for i in range(len(nums)):
        try:
            if nums[i+1] - nums[i] != 1:
                print(nums[i]+1)
                flag_intre = 1
                break
        except IndexError:
            pass


if flag_intre == 0 and flag_start == 0:
    print(nums[-1]+1)