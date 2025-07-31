haystack = "sadbutsad"
needle = "sad"
element_find_num = haystack.count(needle)

index = 0
word = ""
final = []

for i in enumerate(haystack):
    if needle[index] == i[1]:
        word += i[1]
        if index < len(needle)-1:
            index += 1
        else:
            index = 0
            if word == needle:
                word = ""
                final.append(i[0]-len(needle)+1)
            else:
                word = ""

print(final) 





