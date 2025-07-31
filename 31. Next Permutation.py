nums = [3,2,1]
flag_asc = 0
flag_desc = 0

for i in range(len(nums)):
 if i < len(nums) - 1:
        if nums[i] < nums[i+1]:
            flag_asc += 1
        else:
            flag_desc +=1

if flag_asc != 0 and flag_desc != 0:
    for i in range(len(nums)):
        if i < len(nums) - 1:
            if nums[i] < nums[i+1]:
                flag = 1
            else:
                flag = 0
                if nums[i+1] < nums[i-1]: 
                    nums[i], nums[i-1] = nums[i-1], nums[i]
                    nums[i:] = sorted(nums[i:])
                    break
                else:
                    nums[i-1], nums[i+1] = nums[i+1], nums[i-1]
                    nums[i:] = sorted(nums[i:])
                    break
elif flag_desc == 0:
    nums[-1], nums[-2] = nums[-2], nums[-1]

elif flag_asc == 0:
    nums.sort()

print(nums)

