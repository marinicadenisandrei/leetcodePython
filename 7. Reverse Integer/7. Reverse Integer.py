x = -123

if x < 0:
    output = "-"
    for i in reversed(list(str(x))[1:]):
        output += i
else:
    output = ""
    for i in reversed(list(str(x))):
        output += i

print(output)

    