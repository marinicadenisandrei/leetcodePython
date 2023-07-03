s = "    fly me to    the moon  "
s = s.split(" ")

s = [i for i in s if i != ""]

print(len(s[-1]))