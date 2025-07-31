# s = "babad"

# # longest = '' if not s else s[0]
# # max_len = 1
# # size = len(s)
# # dp=[[False]*size for _ in range(size)]
# # for start in range(size-1,-1,-1):
# #     dp[start][start]=True
# #     for end in range(start+1,size):
# #         if s[start]==s[end]:
# #             if end - start == 1 or dp[start+1][end-1]:
# #                 dp[start][end] = True
# #                 if max_len < end - start + 1:
# #                     max_len = end - start + 1
# #                     longest = s[start: end+ 1]

# # print(longest)

# #metoda 2
# def longestPalindrome(s):
#         longest_palindrom = ''
#         dp = [[0]*len(s) for _ in range(len(s))]
#         #filling out the diagonal by 1
#         for i in range(len(s)):
#             dp[i][i] = True
#             longest_palindrom = s[i]
        
#         # filling the dp table
#         for i in range(len(s)-1,-1,-1):
# 				# j starts from the i location : to only work on the upper side of the diagonal 
#             for j in range(i+1,len(s)):  
#                 if s[i] == s[j]:  #if the chars mathces
#                     # if len slicied sub_string is just one letter if the characters are equal, we can say they are palindomr dp[i][j] =True 
#                     #if the slicied sub_string is longer than 1, then we should check if the inner string is also palindrom (check dp[i+1][j-1] is True)
#                     if j-i ==1 or dp[i+1][j-1] is True:
#                         dp[i][j] = True
#                         # we also need to keep track of the maximum palindrom sequence 
#                         if len(longest_palindrom) < len(s[i:j+1]):
#                             longest_palindrom = s[i:j+1]
                
        # return longest_palindrom

# print(longestPalindrome(s))


# longest_pal = ""
# list_of_lists = [[0]* len(s) for _ in range(len(s))]

# for i in range(len(s)):
#     list_of_lists[i][i] = True 
#     longest_pal = s[i]

# for i in range(len(s)-1,-1,-1):
#     for j in range(i+1, len(s)):
#         print("i=",i,"s[i]=",s[i]," - ","j=",j,"s[j]=",s[j])
#         if s[i] == s[j]:
#             if i-j == 1 or list_of_lists[i+1][j-1] == True:
#                 list_of_lists[i] == list_of_lists[j]
#                 if len(longest_palindrom) < len(s[i:j+1]):
#                             longest_palindrom = s[i:j+1]

s = "babad"

longest_pal = ""
list_of_lists = [[0]*len(s) for _ in range(len(s))]

for i in range(len(s)):
    list_of_lists[i][i] = True
    longest_pal = s[i]

for i in range(len(s)-1,-1,-1):
    for j in range(i+1, len(s)):
        if s[i] == s[j] or list_of_lists[i+1][j-1] == True:
            list_of_lists[i][j] == True
            if len(longest_pal) < len(s[i:j+1]):
                longest_pal = s[i:j+1]

print(longest_pal)