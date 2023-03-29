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