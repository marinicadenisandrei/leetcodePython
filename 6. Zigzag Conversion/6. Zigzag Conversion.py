s = "PAYPALLISHIRING"
numRows = 4

col = []
diag = []
row = []

for i in range(0,len(s)):
    if i <= numRows:
        col.append(s[i])
    if i <= numRows + int(numRows/2):
        diag.append(s[i])

print(diag)

    