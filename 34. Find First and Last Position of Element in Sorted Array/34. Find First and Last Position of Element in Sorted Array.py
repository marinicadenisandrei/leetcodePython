nums = [5,7,7,8,8,10]
target = 8

final = None
final2 = None

for i in range(len(nums)):
    if nums[i] == target and final == None:
        final = i
    if nums[-i] == target and final2 == None:
        final2 = len(nums) - i

if final == None and final2 == None:
    final = -1
    final2 = -1

print([final, final2])