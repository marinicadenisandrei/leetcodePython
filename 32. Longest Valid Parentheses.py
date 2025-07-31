s = ")()())"

counter = 0
for i in range(len(s)):
    if s[i] == "(" and s[i+1] == ")":
        counter += 2

print(counter)