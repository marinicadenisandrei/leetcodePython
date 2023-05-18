rule = {
    "(": ")",
    "[": "]",
    "{": "}"
}

flag = False

s = "{}{}{}{}{}{}()[]"
if len(s) % 2 != 0:
        flag == False
else:
    for i,j in zip(range(0,len(s),2), range(1,len(s),2)):
        if s[i] in rule and s[j] == rule[s[i]]:
            flag = True
        else:
            flag = False

print(flag)