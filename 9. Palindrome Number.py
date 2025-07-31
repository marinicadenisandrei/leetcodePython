x = 122

def nr_pali(nr):
    for i,j in zip(str(nr), reversed(str(nr))):
        if i == j:
            return True
        else:
            return False

if nr_pali(x):
    print("Numarul este palindrom")
else:
    print("Numarul nu este palindrom")


    