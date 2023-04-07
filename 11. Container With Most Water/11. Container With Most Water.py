# height = [1,8,6,2,5,4,8,3,7]
height = [1,1]

areas = []

if len(height) == 2:
    if height[0] <= height[1]:
        areas.append(height[0]*1)
else:
    for i in range(len(height)-1):
        for j in range(1,len(height)-1):
            # print("i=",i,height[i], "-", "j=",j,height[j])
            if height[i] < height[j]:
                areas.append(height[i]*i+1)
            else:
                areas.append(height[j]*i+1)



print(max(areas))