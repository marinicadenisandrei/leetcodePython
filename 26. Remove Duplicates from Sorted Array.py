nums = [0,0,1,1,1,2,2,3,3,4]

dictionar = {}

for i in nums:
    if str(i) in dictionar:
        dictionar[str(i)].append(str(i))
    else:
        dictionar[str(i)] = []

nums = [i for i in dictionar.keys()]
final = ["_" for i in dictionar.values()]
nums.extend(final)

print(nums)
