s = "aabb"
p = "a*b*"

match_list = []
former = ""

flag = False

for i in range(len(p)):
    if p[i] == "*":
        for j in range(len(s)):
            former += p[i-1]
            match_list.append(former)
            
        match_list.append(former)
    
    former = ""
    
for i in match_list:
    for j in match_list:
        former = i+j
        match_list.append(former)
        former = ""
        

# if s in match_list:
#     print("True")
# else:
#     for i in range(len(s)):
#         for j in range(i,i+1):
#             if s[i] == p[j] or p[j] == "?" or p[j] == ".":
#                 flag = True
#             else:
#                 flag = False
#                 break
#         if flag == False:
#             break
        
#     print(flag)

# print(match_list)

if s in match_list:
    print("yes")

        
        