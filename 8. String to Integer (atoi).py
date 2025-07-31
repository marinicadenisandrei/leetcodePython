s = "bwijfievwfvewfwe-445355dbcsdbv"
s = "".join([str(i) for i in list(s) if i.isdigit() or i == "-"])

if "-" in s and s[0] != "-":
    s = s.replace("-","")

print(s)